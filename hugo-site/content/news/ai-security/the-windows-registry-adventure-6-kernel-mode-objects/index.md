---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2025-12-13T12:03:14.170006+00:00'
exported_at: '2025-12-13T12:03:17.617002+00:00'
feed: https://googleprojectzero.blogspot.com/feeds/posts/default
language: en
source_url: https://googleprojectzero.blogspot.com/2025/04/the-windows-registry-adventure-6-kernel.html
structured_data:
  about: []
  author: ''
  description: '  Posted by Mateusz Jurczyk, Google Project Zero     Welcome back
    to the Windows Registry Adventure! In the previous installment  of the ser...'
  headline: 'The Windows Registry Adventure #6: Kernel-mode objects'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://googleprojectzero.blogspot.com/2025/04/the-windows-registry-adventure-6-kernel.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: 'The Windows Registry Adventure #6: Kernel-mode objects'
updated_at: '2025-12-13T12:03:14.170006+00:00'
url_hash: 6a0dc862f686b7c56a28937fdc26a6176b3616a3
---

Posted by Mateusz Jurczyk, Google Project Zero

Welcome back to the Windows Registry Adventure! In the

[previous installment](https://googleprojectzero.blogspot.com/2024/12/the-windows-registry-adventure-5-regf.html)

of the series

, we took a deep look into the internals of the regf hive format. Understanding this foundational aspect of the registry is crucial, as it illuminates the design principles behind the mechanism, as well as its inherent strengths and weaknesses. The data stored within the regf file represents the definitive state of the hive. Knowing how to parse this data is sufficient for handling static files encoded in this format, such as when writing a custom regf parser to inspect hives extracted from a hard drive. However, for those interested in how regf files are managed by Windows at runtime, rather than just their behavior in isolation, there's a whole other dimension to explore: the multitude of kernel-mode objects allocated and maintained throughout the lifecycle of an active hive. These auxiliary objects are essential for several reasons:

* To track all currently loaded hives, their properties (e.g., load flags), their memory mappings, and the relationships between them (especially for delta hives overlaid on top of each other).
* To synchronize access to keys and hives within the multithreaded Windows environment.
* To cache hive information for faster access compared to direct memory mapping lookups.
* To integrate the registry with the NT Object Manager and support standard operations (opening/closing handles, setting/querying security descriptors, enforcing access checks, etc.).
* To manage the state of pending transactions before they are fully committed to the underlying hive.

To address these diverse requirements, the Windows kernel employs numerous interconnected structures. In this post, we will examine some of the most critical ones, how they function, and how they can be effectively enumerated and inspected using WinDbg. It's important to note that Microsoft provides official definitions only for some registry-related structures through PDB symbols for ntoskrnl.exe. In many cases, I had to reverse-engineer the relevant code to recover structure layouts, as well as infer the types and names of particular fields and enums. Throughout this write-up, I will clearly indicate whether each structure definition is official or reverse-engineered. If you spot any inaccuracies, please let me know. The definitions presented here are primarily derived from Windows Server 2019 with the March 2022 patches (kernel build 10.0.17763.2686), which was the kernel version used for the majority of my registry code analysis. However, over 99% of registry structure definitions appear to be identical between this version and the latest Windows 11, making the information directly applicable to the latest systems as well.

## Hive structures

Given that hives are the most intricate type of registry object, it's not surprising that their kernel-mode descriptors are equally complex and lengthy. The primary hive descriptor structure in Windows, known as \_CMHIVE, spans a substantial 0x12F8 bytes – exceeding 4 KiB, the standard memory page size on x86-family architectures. Contained within \_CMHIVE, at offset 0, is another structure of type \_HHIVE, which occupies 0x600 bytes, as depicted in the diagram below:

[![Diagram depicting the layout of the Windows Registry kernel structure _CMHIVE. It shows the overall _CMHIVE block, marked with a total size of 0x12F8 bytes. Within this block, the first part, from offset 0x0 to 0x600, is labeled as the _HHIVE structure. The remaining portion, from offset 0x600 to 0x12F8, is labeled "Rest of _CMHIVE".](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhIE8uHd2DJ-gPQVj9KpjdpoVP-aLCdRXjAU0lIpKprgSI3KpFkoomVyU2PvhTA3zp_8ha28xuZUoXTTKKJjyevXRUf2NQ_NaJlHMoPx91KfE6UBsoyKl-VnRbA73_AjPxTf4ZXasUNMAwMKh3kc9VTWczg0ua_9ltU9G1BK7I4xEIHpJ9ubrxah9Jds5U/s1200/image1.png "Diagram depicting the layout of the Windows Registry kernel structure _CMHIVE. It shows the overall _CMHIVE block, marked with a total size of 0x12F8 bytes. Within this block, the first part, from offset 0x0 to 0x600, is labeled as the _HHIVE structure. The remaining portion, from offset 0x600 to 0x12F8, is labeled \"Rest of _CMHIVE\".")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhIE8uHd2DJ-gPQVj9KpjdpoVP-aLCdRXjAU0lIpKprgSI3KpFkoomVyU2PvhTA3zp_8ha28xuZUoXTTKKJjyevXRUf2NQ_NaJlHMoPx91KfE6UBsoyKl-VnRbA73_AjPxTf4ZXasUNMAwMKh3kc9VTWczg0ua_9ltU9G1BK7I4xEIHpJ9ubrxah9Jds5U/s1200/image1.png)

This relationship mirrors that of other common Windows object pairs, such as \_EPROCESS / \_KPROCESS and \_ETHREAD / \_KTHREAD. Because \_HHIVE is always allocated as a component of the larger \_CMHIVE structure, their pointer types are effectively interchangeable. If you encounter a decompiled access using a \_HHIVE\*

pointer

that extends beyond the size of the structure, it almost certainly indicates a reference to a field within the encompassing \_CMHIVE object.

But why are two distinct structures dedicated to representing a single registry hive? While technically not required, this separation likely serves to delineate fields associated with different abstraction layers of the hive. Specifically:

* \_HHIVE manages the low-level aspects of the hive, including the hive header, bins, and cells, as well as in-memory mappings and synchronization state with its on-disk counterpart (e.g., dirty sectors).
* \_CMHIVE handles more abstract information about the hive, such as the cache of security descriptors, pointers to high-level kernel objects like the root Key Control Block (KCB), and the associated transaction resource manager (\_CM\_RM structure).

The next subsections will provide a deeper look into the responsibilities and inner workings of these two structures.

### \_HHIVE structure overview

The primary role of the \_HHIVE structure is to manage the memory-related state of a hive. This allows higher-level registry code to perform operations such as allocating, freeing, and marking cells as "dirty" without needing to handle the low-level implementation details. The \_HHIVE structure comprises 49 top-level members, most of which will be described in larger groups below:

0:



kd>



dt



\_HHIVE

nt!\_HHIVE

+0x000



Signature



:



Uint4B

+0x008



GetCellRoutine



:



Ptr64



\_CELL\_DATA\*

+0x010



ReleaseCellRoutine



:



Ptr64



void

+0x018



Allocate



:



Ptr64



void\*

+0x020



Free



:



Ptr64



void

+0x028



FileWrite



:



Ptr64



long

+0x030



FileRead



:



Ptr64



long

+0x038



HiveLoadFailure



:



Ptr64



Void

+0x040



BaseBlock



:



Ptr64



\_HBASE\_BLOCK

+0x048



FlusherLock



:



\_CMSI\_RW\_LOCK

+0x050



WriterLock



:



\_CMSI\_RW\_LOCK

+0x058



DirtyVector



:



\_RTL\_BITMAP

+0x068



DirtyCount



:



Uint4B

+0x06c



DirtyAlloc



:



Uint4B

+0x070



UnreconciledVector



:



\_RTL\_BITMAP

+0x080



UnreconciledCount



:



Uint4B

+0x084



BaseBlockAlloc



:



Uint4B

+0x088



Cluster



:



Uint4B

+0x08c



Flat



:



Pos



0,



1



Bit

+0x08c



ReadOnly



:



Pos



1,



1



Bit

+0x08c



Reserved



:



Pos



2,



6



Bits

+0x08d



DirtyFlag



:



UChar

+0x090



HvBinHeadersUse



:



Uint4B

+0x094



HvFreeCellsUse



:



Uint4B

+0x098



HvUsedCellsUse



:



Uint4B

+0x09c



CmUsedCellsUse



:



Uint4B

+0x0a0



HiveFlags



:



Uint4B

+0x0a4



CurrentLog



:



Uint4B

+0x0a8



CurrentLogSequence



:



Uint4B

+0x0ac



CurrentLogMinimumSequence



:



Uint4B

+0x0b0



CurrentLogOffset



:



Uint4B

+0x0b4



MinimumLogSequence



:



Uint4B

+0x0b8



LogFileSizeCap



:



Uint4B

+0x0bc



LogDataPresent



:



[2]



UChar

+0x0be



PrimaryFileValid



:



UChar

+0x0bf



BaseBlockDirty



:



UChar

+0x0c0



LastLogSwapTime



:



\_LARGE\_INTEGER

+0x0c8



FirstLogFile



:



Pos



0,



3



Bits

+0x0c8



SecondLogFile



:



Pos



3,



3



Bits

+0x0c8



HeaderRecovered



:



Pos



6,



1



Bit

+0x0c8



LegacyRecoveryIndicated



:



Pos



7,



1



Bit

+0x0c8



RecoveryInformationReserved



:



Pos



8,



8



Bits

+0x0c8



RecoveryInformation



:



Uint2B

+0x0ca



LogEntriesRecovered



:



[2]



UChar

+0x0cc



RefreshCount



:



Uint4B

+0x0d0



StorageTypeCount



:



Uint4B

+0x0d4



Version



:



Uint4B

+0x0d8



ViewMap



:



\_HVP\_VIEW\_MAP

+0x110



Storage



:



[2]



\_DUAL

#### Signature

Equal to 0xBEE0BEE0, it is a unique signature of the \_HHIVE / \_CMHIVE structures. It may be useful in digital forensics for identifying these structures in raw memory dumps, and is yet another

[reference to bees](https://devblogs.microsoft.com/oldnewthing/20030808-00/?p=42943)

in the Windows registry implementation.

#### Function pointers

Next up, there are six function pointers, initialized in HvHiveStartFileBacked and HvHiveStartMemoryBacked, and pointing at internal kernel handlers for the following operations:

|  |  |  |
| --- | --- | --- |
| Pointer name | Pointer value | Operation |
| GetCellRoutine | HvpGetCellPaged or HvpGetCellFlat | Translate cell index to virtual address |
| ReleaseCellRoutine | HvpReleaseCellPaged or HvpReleaseCellFlat | Release  previously translated cell index |
| Allocate | CmpAllocate | Allocate kernel memory within global registry quota |
| Free | CmpFree | Free kernel memory within global registry quota |
| FileWrite | CmpFileWrite | Write data to hive file |
| FileRead | CmpFileRead | Read data from hive file |

As we can see, these functions provide the basic functionality of operating on kernel memory, cell indexes, and the hive file. In my opinion, the most important of them is GetCellRoutine, whose typical destination, HvpGetCellPaged, performs the

cell map walk

in order to translate a cell index into the corresponding address within the hive mapping.

It is natural to think that these function pointers could prove useful for exploitation if an attacker managed to corrupt them through a buffer overflow or a use-after-free condition. That was indeed the case in Windows 10 and earlier, but in Windows 11, these calls are now de-virtualized, and most call sites reference one of HvpGetCellPaged / HvpGetCellFlat and HvpReleaseCellPaged / HvpReleaseCellFlat directly, without referring to the pointers. This is great for security, as it completely eliminates the usefulness of those fields in any offensive scenarios.

Here's an example of a GetCellRoutine call in Windows 10, disassembled in IDA Pro:

[![IDA Pro disassembly view showing assembly code related to the GetCellRoutine call in Windows 10, featuring mov and lea instructions, cross-references to CmSetValueKey, and culminating in a call to __guard_dispatch_icall.](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh3E0Bw87KBmn8O14C3MXMvGS_OKgSuW6gv0KYqUXTA1DroYV-fPxaRxwbQYYKEMVIdfJd2XJ7MSTkUhiKl9JCPoOWByIsuSwylGe5bs08UbSRYn9jZQxIizAVJgAxMJGC6R01h2wFMeeypsKrMgPYbbdTNJhjYdEvFhzxUmVV5n9iYSY32X8WOU5fZAYk/s1200/image11.png "IDA Pro disassembly view showing assembly code related to the GetCellRoutine call in Windows 10, featuring mov and lea instructions, cross-references to CmSetValueKey, and culminating in a call to __guard_dispatch_icall.")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh3E0Bw87KBmn8O14C3MXMvGS_OKgSuW6gv0KYqUXTA1DroYV-fPxaRxwbQYYKEMVIdfJd2XJ7MSTkUhiKl9JCPoOWByIsuSwylGe5bs08UbSRYn9jZQxIizAVJgAxMJGC6R01h2wFMeeypsKrMgPYbbdTNJhjYdEvFhzxUmVV5n9iYSY32X8WOU5fZAYk/s1200/image11.png)

And the same call in Windows 11:

[![IDA Pro disassembly of a GetCellRoutine call implementation in Windows 11. The assembly code shows register setup (mov, lea), a test instruction followed by a conditional jump (jz). Depending on the condition, the code either calls HvlpGetCellFlat and jumps onward, or calls HvlpGetCellPaged. Cross-references to CmSetValueKey are also shown](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEioyK0W61kSNa18Sj0Habbo8I5B3pqJSjtWE4MceBYzi3QHsS-m4tvgi9eh16DETfrouRwahyfrStRpRR_eDRf0-_V0Ix8o-Y544klhS9Fy3iR1sOXnmF1gstjmgI-5S-Ybv1jmTH0c0oE0PQJXA6CbFD2nIRrXJ4SnKkif7NZ7OUKVVXc2nRotmvqe0Y0/s1200/image3.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEioyK0W61kSNa18Sj0Habbo8I5B3pqJSjtWE4MceBYzi3QHsS-m4tvgi9eh16DETfrouRwahyfrStRpRR_eDRf0-_V0Ix8o-Y544klhS9Fy3iR1sOXnmF1gstjmgI-5S-Ybv1jmTH0c0oE0PQJXA6CbFD2nIRrXJ4SnKkif7NZ7OUKVVXc2nRotmvqe0Y0/s1200/image3.png)

#### Hive load failure information

This is a pointer to a public \_HIVE\_LOAD\_FAILURE structure, which is passed as the first argument to the SetFailureLocation function every time an error occurs while loading a hive. It can be helpful in tracking which validity checks have failed for a given hive, without having to trace the entire loading process.

#### Base block

A pointer to a copy of the hive header, represented by the \_HBASE\_BLOCK structure.

#### Synchronization locks

There are two locks with the following purpose:

* FlusherLock – synchronizes access to the hive between clients changing data inside cells and the flusher thread;
* WriterLock – synchronizes access to the hive between writers that modify the bin/cell layout.

They are officially of type \_CMSI\_RW\_LOCK, but they boil down to \_EX\_PUSH\_LOCK, and they are used with standard kernel APIs such as ExAcquirePushLockSharedEx.

#### Dirty blocks information

Between offsets 0x58 and 0x84, \_HHIVE stores several data structures representing the state of synchronization between the in-memory and on-disk instances of the hive.

#### Hive flags

First of all, there are two flags at offset 0x8C that indicate if the hive mapping is flat and if the hive is read-only. Secondly, there is a 32-bit HiveFlags member that stores further flags which aren't (as far as I know) included in any public Windows symbols. I have managed to reverse-engineer and infer the meaning of the constants I have observed, resulting in the following enum:

enum



\_HV\_HIVE\_FLAGS

{

HIVE\_VOLATILE



=



0x1

,

HIVE\_NOLAZYFLUSH



=



0x2

,

HIVE\_PRELOADED



=



0x10

,

HIVE\_IS\_UNLOADING



=



0x20

,

HIVE\_COMPLETE\_UNLOAD\_STARTED



=



0x40

,

HIVE\_ALL\_REFS\_DROPPED



=



0x80

,

HIVE\_ON\_PRELOADED\_LIST



=



0x400

,

HIVE\_FILE\_READ\_ONLY



=



0x8000

,

HIVE\_SECTION\_BACKED



=



0x20000

,

HIVE\_DIFFERENCING



=



0x80000

,

HIVE\_IMMUTABLE



=



0x100000

,

HIVE\_FILE\_PAGES\_MUST\_BE\_KEPT\_LOCAL



=



0x800000

,

};

Below is a one-liner explanation of each flag:

* HIVE\_VOLATILE:

  the hive exists in memory only; set, e.g., for \Registry and \Registry\Machine\HARDWARE.
* HIVE\_NOLAZYFLUSH:

  changes to the hive aren't automatically flushed to disk and require a manual flush; set, e.g., for \Registry\Machine\SAM.
* HIVE\_PRELOADED:

  the hive is one of the default, system ones; set, e.g., for \Registry\Machine\SOFTWARE, \Registry\Machine\SYSTEM, etc.
* HIVE\_IS\_UNLOADING:

  the hive is currently being loaded or unloaded in another thread and shouldn't be accessed before the operation is complete.
* HIVE\_COMPLETE\_UNLOAD\_STARTED:

  the unloading process of the hive has started in CmpCompleteUnloadKey.
* HIVE\_ALL\_REFS\_DROPPED:

  all references to the hive through KCBs have been dropped.
* HIVE\_ON\_PRELOADED\_LIST:

  the hive is linked into a linked-list via the PreloadedHiveList field.
* HIVE\_FILE\_READ\_ONLY:

  the underlying hive file is read-only and shouldn't be modified; indicates that the hive was loaded with the REG\_OPEN\_READ\_ONLY flag set.
* HIVE\_SECTION\_BACKED:

  the hive is mapped in memory using section views.
* HIVE\_DIFFERENCING:

  the hive is a differencing one (version 1.6, loaded under \Registry\WC).
* HIVE\_IMMUTABLE:

  the hive is immutable and cannot be modified; indicates that it was loaded with the REG\_IMMUTABLE flag set.
* HIVE\_FILE\_PAGES\_MUST\_BE\_KEPT\_LOCAL:

  the kernel always maintains a local copy of every page of the hive, either by locking it in physical memory or creating a private copy through the CoW mechanism.

#### Log file information

Between offsets 0xA4 to 0xCC, there are a number of fields having to do with log file management, i.e. the .LOG1/.LOG2 files accompanying the main hive file on disk.

#### Hive version

The Version field stores the minor version of the hive, which should theoretically be an integer between 3–6. However, as mentioned in the

[previous blog post](https://googleprojectzero.blogspot.com/2024/12/the-windows-registry-adventure-5-regf.html)

, it is possible to set it to an arbitrary 32-bit value either by specifying a major version equal to 0 and any desired minor version, or by enticing the kernel to recover the hive header from a log file, and abusing the fact that the HvAnalyzeLogFiles function is more permissive than HvpGetHiveHeader. Nevertheless, I haven't found any security implications of this behavior.

#### View map

The view map holds all the essential information about how the hive is mapped in memory. The specific implementation of registry memory management has evolved considerably over the years, with its details changing between consecutive system versions. In the latest ones, the view map is represented by the top-level \_HVP\_VIEW\_MAP public structure:

0:



kd>



dt



\_HVP\_VIEW\_MAP

nt!\_HVP\_VIEW\_MAP

+0x000



SectionReference



:



Ptr64



Void

+0x008



StorageEndFileOffset



:



Int8B

+0x010



SectionEndFileOffset



:



Int8B

+0x018



ProcessTuple



:



Ptr64



\_CMSI\_PROCESS\_TUPLE

+0x020



Flags



:



Uint4B

+0x028



ViewTree



:



\_RTL\_RB\_TREE

The semantics of its respective fields are as follows:

* SectionReference:

  Contains a kernel-mode handle to a section object corresponding to the hive file, created via ZwCreateSection in CmSiCreateSectionForFile.
* StorageEndFileOffset:

  Stores the maximum size of the hive that can be represented with file-backed sections at any given time. Initially set to the size of the loaded hive, it can dynamically increase or decrease at runtime for mutable (normal) hives.
* SectionEndFileOffset:

  Represents the size of the hive file section at the time of loading. It is never modified past the first initialization in HvpViewMapStart, and seems to be mostly used as a safeguard against extending an immutable hive file beyond its original size.
* ProcessTuple:

  A structure of type \_CMSI\_PROCESS\_TUPLE, it identifies the host process of the hive's section views. This field currently always points to the global CmpRegistryProcess object, which corresponds to the dedicated "Registry" process that hosts all hive mappings in the system. However, this field could enable a more fine-grained separation of hive mappings across multiple processes, should Microsoft choose to implement such a feature.
* Flags:

  Represents a set of memory management flags relevant to the entire hive.

  These flags are not publicly documented; however, through reverse engineering, I have determined their purpose

  to be as follows:

* VIEW\_MAP\_HIVE\_FILE\_IMMUTABLE

  (0x1): Indicates that the hive has been loaded as immutable, meaning no data is ever saved back to the underlying hive file.
* VIEW\_MAP\_MUST\_BE\_KEPT\_LOCAL

  (0x2): Indicates that all of the hive data must be persistently stored in memory, and not just accessible through file-backed sections. This is likely to protect against double-fetch conditions involving hives loaded from remote network shares.
* VIEW\_MAP\_CONTAINS\_LOCKED\_PAGES

  (0x4): Indicates that some of the hive's pages are currently locked in physical memory using ZwLockVirtualMemory.

* ViewTree:

  This is the root of a view tree structure, which contains the descriptors of each continuous section view mapped in memory.

Overall, the implementation of low-level hive memory management in Windows is more complex than might initially seem necessary. This complexity arises from the kernel's need to gracefully handle a variety of corner cases and interactions. For example, hives may be loaded as immutable, which indicates that the hive may be operated on in memory, but changes must not be flushed to disk. Simultaneously, the system must support recovering data from .LOG files, including the possibility of extending the hive beyond its original on-disk length. At runtime, it must also be possible to efficiently modify the registry data, as well as shrink and extend it on demand. To further complicate matters, Windows enforces different rules for locking hive pages in memory depending on the backing volume of the file, carefully balancing optimal memory usage and system security guarantees. These and many other factors collectively contribute to the complexity of hive memory management.

To better understand how the view tree is organized, let's first analyze the general logic of the hive mapping code.

##### The hive mapping logic

The main kernel function responsible for mapping a hive in memory is HvLoadHive. It implements the overall logic and coordinates various sub-routines responsible for performing more specialized tasks, in the following order:

1. Header Validation:

   The kernel reads and inspects the hive's header to ascertain its integrity, ensuring that the hive has not been tampered with or corrupted. Relevant function: HvpGetHiveHeader.
2. Log Analysis:

   The kernel processes the hive's transaction logs, scrutinising them to identify any pending changes or inconsistencies that necessitate recovery procedures. Relevant function: HvAnalyzeLogFiles.
3. Initial Section Mapping:

   A section object is created based on the hive file, and further segmented into multiple views, each aligned to 4 KiB boundaries and capped at 2 MiB. At this point, the kernel prioritizes the creation of an initial mapping without focusing on the granular layout of individual bins within the hive. Relevant function: HvpViewMapStart.
4. Cell Map Initialization:

   The cell map, a component that translates cell indexes to memory address, is initialized. Its entries are configured to point to the newly created views. Relevant function: HvpMapHiveImageFromViewMap.
5. Log Recovery (if required):

   If the preceding log analysis reveals the need for data recovery, the kernel attempts to restore data integrity. This is the earliest point at which the newly created memory mappings may already be modified and marked as "dirty", indicating that their contents have been altered and require synchronisation with the on-disk representation. Relevant function: HvpPerformLogFileRecovery.
6. Bin Mapping:

   In this final stage, the kernel establishes definitive memory mappings for each bin within the hive, ensuring that each bin occupies a contiguous region of memory. This process may necessitate creating new views, eliminating existing ones, or adjusting their boundaries to accommodate the specific arrangement of bins. Relevant function: HvpRemapAndEnlistHiveBins.

Now that we understand the primary components of the loading process, we can examine the internal structure of the section view tree in more detail.

##### The view tree

Let's consider an example hive consisting of three bins of sizes 256 KiB, 2 MiB and 128 KiB, respectively. After step 3 ("Initial Section Mapping"), the section views created by the kernel are as follows:

[![Diagram illustrating the initial section view layout for a sample Windows Registry hive. The top section shows the hive layout with Header, Bin 1 (256 KB), Bin 2 (2 MB), and Bin 3 (128 KB). The bottom section shows the corresponding initial kernel mapping: View 1 (1.996 MiB) spanning Bin 1 and most of Bin 2, and View 2 (388 KiB) spanning the end of Bin 2 and Bin 3.](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhiTuUvYZQNPVdfvmgXJ3hZD2jkrKCL0sLjCfoTfBC1LDW52m4zNpR7GffCZZ4kUwO0rFIQr0jKfhWqKHpqROqrMW5oOovM75P6gdM-hwUwxYKYHK5z5BMvPFemvTybE9PNmJORN27zhr2WVOa3orx5V3oW8njq2DFT2idGnipovJVhtC-EBBXfnEg06gk/s1200/image5.png "Diagram illustrating the initial section view layout for a sample Windows Registry hive. The top section shows the hive layout with Header, Bin 1 (256 KB), Bin 2 (2 MB), and Bin 3 (128 KB). The bottom section shows the corresponding initial kernel mapping: View 1 (1.996 MiB) spanning Bin 1 and most of Bin 2, and View 2 (388 KiB) spanning the end of Bin 2 and Bin 3.")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhiTuUvYZQNPVdfvmgXJ3hZD2jkrKCL0sLjCfoTfBC1LDW52m4zNpR7GffCZZ4kUwO0rFIQr0jKfhWqKHpqROqrMW5oOovM75P6gdM-hwUwxYKYHK5z5BMvPFemvTybE9PNmJORN27zhr2WVOa3orx5V3oW8njq2DFT2idGnipovJVhtC-EBBXfnEg06gk/s1200/image5.png)

As we can see, at this point, the kernel doesn't concern itself with bin boundaries or continuity: all it needs to achieve is to make every page of the hive accessible through a section view for log recovery purposes. In simple terms, the way that HvpViewMapStart (or more specifically, HvpViewMapCreateViewsForRegion) works is it creates as many 2 MiB views as necessary, followed by one last view that covers the remaining part of the file. So in our example, we have the first view that covers bin 1 and the beginning of bin 2, and the second view that covers the trailing part of bin 2 and the entire bin 3. It's important to note that memory continuity is only guaranteed within the scope of a single view, and views 1 and 2 may be mapped at completely different locations in the virtual address space.

Later in step 6, the system ensures that every bin is mapped as a contiguous block of memory before handing off the hive to the client. This is done by iterating through all the bins, and for every bin that spans more than one view in the current view map, the following operations are performed:

* If the start and/or the end of the bin fall into the middle of existing views, these views are truncated from either side. Furthermore, if there are any views that are fully covered by the bin, they are freed and removed from the tree.
* A new, dedicated section view is created for the bin and inserted into the view tree.

In our hypothetical scenario, the resulting view layout would be as follows:

[![Diagram showing a Windows Registry hive layout divided into Header, Bin 1 (256KB), Bin 2 (2MB), and Bin 3 (128KB), with a corresponding section view layout illustrating how View 1, View 2, and View 3 map onto these bins.](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhmc_KkJaExe8Vfkwfj8CF9-yH18v_DnuxuZosaHxRTfmxgppFDz3um9WC7NlOeH3I8ShvUK-aRuXfyuJWnYbsV658dG7lk67kj5Q4oHE4-sLCBo3znyXzzEDjxKsmWtf5HGVdVt4sl0CmYrojlGZim72ypaHRf_14wypnTdjSYExHs5JGQVuAOLyPoZ8Q/s1200/image12.png "Diagram showing a Windows Registry hive layout divided into Header, Bin 1 (256KB), Bin 2 (2MB), and Bin 3 (128KB), with a corresponding section view layout illustrating how View 1, View 2, and View 3 map onto these bins.")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhmc_KkJaExe8Vfkwfj8CF9-yH18v_DnuxuZosaHxRTfmxgppFDz3um9WC7NlOeH3I8ShvUK-aRuXfyuJWnYbsV658dG7lk67kj5Q4oHE4-sLCBo3znyXzzEDjxKsmWtf5HGVdVt4sl0CmYrojlGZim72ypaHRf_14wypnTdjSYExHs5JGQVuAOLyPoZ8Q/s1200/image12.png)

As we can see, the kernel shrinks views 1 and 2, and creates a new view 3 corresponding to bin 2 to fill the gap. The final layout of the binary tree of section view descriptors is illustrated below:

[![Diagram showing the final binary tree layout of section view descriptors for a Windows Registry hive. View 3 is the root node, with View 1 as the left child and View 2 as the right child. Each node box displays the specific valid and overall memory address ranges (in hexadecimal) associated with that view descriptor.](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgEn3ezfZPi1NDmErHLk1Y36SK663Fqj7A0PAyu78FM0dekYMIu_fvN3Fq7t4lLjxUPm1VMuPgDVjfFQWxMGxqvPAcmT7C2JwjrnzpLcy39ViRrAQYpP7xlhZO-rw1lN8wbg65z3xDwxDW2qRxWIuTmYmV1XpKHcc2JiPT0yg6CcE_oD7RGLNHuuNCxBJc/s1200/image7.png "Diagram showing the final binary tree layout of section view descriptors for a Windows Registry hive. View 3 is the root node, with View 1 as the left child and View 2 as the right child. Each node box displays the specific valid and overall memory address ranges (in hexadecimal) associated with that view descriptor.")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgEn3ezfZPi1NDmErHLk1Y36SK663Fqj7A0PAyu78FM0dekYMIu_fvN3Fq7t4lLjxUPm1VMuPgDVjfFQWxMGxqvPAcmT7C2JwjrnzpLcy39ViRrAQYpP7xlhZO-rw1lN8wbg65z3xDwxDW2qRxWIuTmYmV1XpKHcc2JiPT0yg6CcE_oD7RGLNHuuNCxBJc/s1200/image7.png)

Knowing this, we can finally examine the structure of a single view tree entry. It is not included in the public symbols, but I named it \_HVP\_VIEW. My reverse-engineered version of its definition is as follows:

struct



\_HVP\_VIEW

{

RTL\_BALANCED\_NODE



Node;

LARGE\_INTEGER



ViewStartOffset;

LARGE\_INTEGER



ViewEndOffset;

SSIZE\_T



ValidStartOffset;

SSIZE\_T



ValidEndOffset;

PBYTE



MappingAddress;

SIZE\_T



LockedPageCount;

\_HVP\_VIEW\_PAGE\_FLAGS



PageFlags[];

};

The role of each particular field is documented below:

* Node:

  This is the structure used to link all of the entries into a single red-black tree, passed to helper kernel functions such as RtlRbInsertNodeEx and RtlRbRemoveNode.
* ViewStartOffset

  and

  ViewEndOffset:

  This offset pair specifies the overall byte range covered by the underlying section view object in the hive file. Their difference corresponds to the cumulative length of the red and green boxes in a single row in the diagrams above.
* ValidStartOffset

  and

  ValidEndOffset:

  This offset pair specifies the

  valid

  range of the hive accessible through this view, i.e. the green rectangles in the diagrams. It must always be a subset of the [ViewStartOffset, ViewEndOffset] range, and may dynamically change while re-mapping bins (as just shown in this section), as well as when shrinking and extending the hive.
* MappingAddress:

  This is the base address of the section view mapping in memory, as returned by ZwMapViewOfSection. It is valid in the context of the process specified by \_HVP\_VIEW\_MAP.ProcessTuple (currently always the "Registry" process). It covers the entire range between [ViewStartOffset, ViewEndOffset], but only pages between [ValidStartOffset, ValidEndOffset] are accessible, and the rest of the section view is marked as PAGE\_NOACCESS.
* LockedPageCount:

  Specifies the number of pages locked in virtual memory using ZwLockVirtualMemory within this view.
* PageFlags:

  A variable-length array that specifies a set of flags for each memory page in the [ViewStartOffset, ViewEndOffset] range.

I haven't found any (un)official sources documenting the set of supported page flags, so below is my attempt to name them and explain their meaning:

|  |  |  |
| --- | --- | --- |
| Flag | Value | Description |
| VIEW\_PAGE\_VALID | 0x1 | Indicates if the page is valid – true for pages between [ValidStartOffset, ValidEndOffset], false otherwise. If this flag is clear, all other flags are irrelevant/unused.    The flag is set:   * When creating section views during hive loading, first the initial ones in HvpViewMapStart, and then the bin-specific ones in HvpRemapAndEnlistHiveBins. * When extending an active hive in HvpViewMapExtendStorage.     The flag is cleared:   * When trimming the existing views in HvpRemapAndEnlistHiveBins to make room for new ones. * When shrinking the hive in HvpViewMapShrinkStorage. |
| VIEW\_PAGE\_COW\_BY\_CALLER | 0x2 | Indicates if the kernel maintains a copy of the page through the copy-on-write (CoW) mechanism, as initiated by a client action, e.g. a registry operation that modified data in a cell and thus resulted in marking the page as dirty.    The flag is set:   * When dirtying a hive cell, in HvpViewMapMakeViewRangeCOWByCaller.     The flag is cleared:   * When flushing the registry changes to disk, in HvpViewMapMakeViewRangeUnCOWByCaller. |
| VIEW\_PAGE\_COW\_BY\_POLICY | 0x4 | Indicates if the kernel maintains a copy of the page through the copy-on-write (CoW) mechanism, as required by the policy that all pages of non-local hives (hives loaded from volumes other than the system volume) must always remain in memory.    The flag is set:   * In HvpViewMapMakeViewRangeValid, as an alternative way of keeping a local copy of the hive pages in memory (if locking fails, or the caller doesn't want the pages locked). * In HvpViewMapMakeViewRangeCOWByCaller, when converting previously locked pages to the "CoW by policy" state. * In HvpMappedViewConvertRegionFromLockedToCOWByPolicy, when lazily converting previously locked pages to the "CoW by policy" state in a thread that runs every 60 seconds (as indicated by CmpLazyLocalizeIntervalInSeconds).     The flag is cleared:   * In HvpViewMapMakeViewRangeUnCOWByPolicy, which currently only ever seems to happen for hives loaded from the system volume, i.e. "\SystemRoot" and "\OSDataRoot", as listed in the global CmpWellKnownVolumeList array. |
| VIEW\_PAGE\_WRITABLE | 0x8 | Indicates if the page is currently marked as writable, typically as a result of a modifying operation on the page that hasn't been yet flushed to disk.    The flag is set:   * In HvpViewMapMakeViewRangeCOWByCaller, when marking a cell as dirty.     The flag is cleared:   * In HvpViewMapMakeViewRangeUnCOWByCaller, when flushing the hive changes to disk. * In HvpViewMapSealRange, when setting the memory as read-only for miscellaneous reasons (after performing log file recovery, etc.). |
| VIEW\_PAGE\_LOCKED | 0x10 | Indicates if the page is currently locked in physical memory.    The flag is set:   * In HvpViewMapMakeViewRangeValid if the caller requests page locking, and there is enough space left in the 64 MiB working set of the Registry process. In practice, this boils down to locking the initial 2 MiB hive mappings created in HvpViewMapStart for all app hives and for normal hives outside of the system disk volume.     The flag is cleared:   * Whenever the state of the page changes to CoW-by-policy or Invalid in the following functions:  * HvpViewMapMakeViewRangeCOWByCaller * HvpMappedViewConvertRegionFromLockedToCOWByPolicy * HvpViewMapMakeViewRangeUnCOWByPolicy * HvpViewMapMakeViewRangeInvalid |

The semantics of most of the flags are straightforward, but perhaps VIEW\_PAGE\_COW\_BY\_POLICY and VIEW\_PAGE\_LOCKED warrant a slightly longer explanation. The two flags are mutually exclusive, and they represent nearly identical ways to achieve the same goal: ensure that a copy of each hive page remains resident in memory or a pagefile. Under normal circumstances, the kernel could simply create the necessary section views in their default form, and let the memory management subsystem decide how to handle their pages most efficiently. However, one of the guarantees of the registry is that once a hive has been loaded, it must remain operational for as long as it is active in the system. On the other hand, section views have the property that (parts of) their underlying data may be completely evicted by the kernel, and later re-read from the original storage medium such as the hard drive. So, it is possible to imagine a situation where:

* A hive is loaded from a removable drive (e.g. a CD-ROM or flash drive) or a network share,
* Due to high memory pressure from other applications, some of the hive pages are evicted from memory,
* The removable drive with the hive file is ejected from the system,
* A client subsequently tries to operate on the hive, but parts of it are unavailable and cannot be fetched again from the original source.

This could cause some significant problems and make the registry code fail in unexpected ways. It would also constitute a security vulnerability: the kernel assumes that once it has opened and sanitized the hive file, its contents remain consistent for as long as the hive is used. This is achieved by opening the file with exclusive access, but if the hive data was ever re-read by the Windows memory manager, a malicious removable drive or an attacker-controlled network share could ignore the exclusivity request and provide different, invalid data on the second read. This would result in a kind of "double fetch" condition and potentially lead to kernel memory corruption.

To address both the reliability and security concerns, Windows makes sure to never evict pages corresponding to hives for which exclusive access cannot be guaranteed. This covers hives loaded from a location other than the system volume, and since Windows 10 19H1, also all app hives regardless of the file location. The first way to achieve this is by locking the pages directly in physical memory with a ZwLockVirtualMemory call. It is used for the initial ≤ 2 MiB section views created while loading a hive, up to the working set limit of the Registry process currently set at 64 MiB. The second way is by taking advantage of the copy-on-write mechanism – that is, marking the relevant pages as

[PAGE\_WRITECOPY](https://learn.microsoft.com/en-us/windows/win32/memory/memory-protection-constants#PAGE_WRITECOPY)

and subsequently touching each of them using the HvpViewMapTouchPages helper function. This causes the memory manager to create a private copy of each memory page containing the same data as the original, thus preventing them from ever being unavailable for registry operations.

Between the two types of resident pages, the CoW type effectively becomes the default option in the long term. Eventually most pages converge to this state, even if they initially start as

locked. This is because locked pages transition to CoW on multiple occasions, e.g. when converted by the background CmpDoLocalizeNextHive thread that runs every 60 seconds, or during the modification of a cell. On the other hand, once a page transitions to the CoW state, it never reverts to being locked. A diagram illustrating the transitions between the page residence states in a hive loaded from removable/remote storage is shown below:

[![State transition diagram illustrating data states like VALID, LOCKED, and COW (Copy-on-Write), and transitions such as load, dirty, and flush, in the context of Windows Registry data management.](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjt-euMQDpGa7-3Cxdej273QDvPm98mUGVm0M_dQvgf-O_DCbJ0Fb9GLKm2X6F4TOnGo6V11CGYtqHhr9221IMWKO4ypXctxoEn0Hzj2OtCo5Vhkbnxr2p9Q-3ebwaOBJcMvZTi8cx8U1p8dr73KLdj6wsxW7FLnpKB-bzSEfPD88mSjifWeEYa6AIKDT4/s1200/image13.png "State transition diagram illustrating data states like VALID, LOCKED, and COW (Copy-on-Write), and transitions such as load, dirty, and flush, in the context of Windows Registry data management.")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjt-euMQDpGa7-3Cxdej273QDvPm98mUGVm0M_dQvgf-O_DCbJ0Fb9GLKm2X6F4TOnGo6V11CGYtqHhr9221IMWKO4ypXctxoEn0Hzj2OtCo5Vhkbnxr2p9Q-3ebwaOBJcMvZTi8cx8U1p8dr73KLdj6wsxW7FLnpKB-bzSEfPD88mSjifWeEYa6AIKDT4/s1200/image13.png)

For normal hives loaded from the system volume (i.e. without the VIEW\_MAP\_MUST\_BE\_KEPT\_LOCAL flag set), the state machine is much simpler:

[![Simplified state machine diagram for normal Windows Registry hive loading (without VIEW_MAP_MUST_BE_KEPT_LOCAL flag). It shows a 'load' action leading to a 'VALID' state. A 'dirty' action transitions to a combined 'VALID/WRITABLE/COW_BY_CALLER' state, and a 'flush' action returns to the 'VALID' state.](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiL-WU3mvLfndmQaY0Ta8y1LCQmWyQdmbpC5yJNNLslyfFMb0LApWGfh8HAsiOh0XcCGz0tjTcZzcY-dkg-GktMsS2sCJfdB11Rq1sBZd3iH7NivRdo2E_oe-AZjaFZProHRsEEniBton6HQR6hs5NOpS8x6Hb3zV8IT-tpiFC5Z3aZxUId5LnbR-UMkOU/s1200/image9.png "Simplified state machine diagram for normal Windows Registry hive loading (without VIEW_MAP_MUST_BE_KEPT_LOCAL flag). It shows a 'load' action leading to a 'VALID' state. A 'dirty' action transitions to a combined 'VALID/WRITABLE/COW_BY_CALLER' state, and a 'flush' action returns to the 'VALID' state.")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiL-WU3mvLfndmQaY0Ta8y1LCQmWyQdmbpC5yJNNLslyfFMb0LApWGfh8HAsiOh0XcCGz0tjTcZzcY-dkg-GktMsS2sCJfdB11Rq1sBZd3iH7NivRdo2E_oe-AZjaFZProHRsEEniBton6HQR6hs5NOpS8x6Hb3zV8IT-tpiFC5Z3aZxUId5LnbR-UMkOU/s1200/image9.png)

As a side note,

[CVE-2024-43452](https://project-zero.issues.chromium.org/issues/42451731)

was an interesting bug that exploited a flaw in the page residency protection logic.



The bug arose because some data wasn't guaranteed to be resident in memory and could be fetched twice from a remote SMB share during bin mapping.



This occurred early in the hive loading process, before page residency protections were fully in place.



The kernel trusted the data from the second read without re-validation, allowing it to be maliciously set to invalid values, resulting in kernel memory corruption.

#### Cell maps

As discussed in

[Part 5](https://googleprojectzero.blogspot.com/2024/12/the-windows-registry-adventure-5-regf.html)

, almost every cell contains references to other cells in the hive in the form of

cell indexes. Consequently, virtually every registry operation involves multiple rounds of translating cell indexes into their corresponding virtual addresses in order to traverse the registry structure. Section views are stored in a red-black tree, so the search complexity is O(log n). This may seem decent, but if we consider that on a typical system, the registry is read much more often than it is extended/shrunk, it becomes apparent that it makes sense to further optimize the search operation at the cost of a less efficient insertion/deletion. And this is exactly what cell maps are: a way of trading a faster search complexity of O(1) for slower insertion/deletion complexity of O(n) instead of O(log n). Thanks to this technique, HvpGetCellPaged – perhaps the hottest function in the Windows registry implementation – executes in constant time.

In technical terms, cell maps are pagetable-like structures that divide the 32-bit hive address space into smaller, nested layers consisting of so-called directories, tables, and entries. As a reminder, the layout of cell indexes and cell maps is illustrated in the diagram below, based on a similar diagram in the Windows Internals book, which itself draws from Mark Russinovich's 1999 article,

[Inside the Registry](https://learn.microsoft.com/en-us/previous-versions//cc750583(v%3Dtechnet.10))

:

[![Diagram illustrating the Windows Registry cell index structure and lookup mechanism, showing how the index's fields (Storage selector, Directory index, Table index, Byte offset) navigate through Storage list, Directory, and Table structures to locate a target Cell block.](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjt4QKKXqrippLUjWNAvXiEPc5Fo6G-_H0CPRusrJQ0vb3Tf2iWyj6wKd7LaWRuzgIwRaq0iyWXhWJPlYIfB120h3gokRyc-MHCEPV8xza2dY7jLqL0dglEy6M5lT9YDlSUcbpF7F8YjgiCEjQEQR8SB7a2KvAECsTyQpgsHCB1eyt3zV7IX42kxY4_ijI/s1200/image10.png "Diagram illustrating the Windows Registry cell index structure and lookup mechanism, showing how the index's fields (Storage selector, Directory index, Table index, Byte offset) navigate through Storage list, Directory, and Table structures to locate a target Cell block.")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjt4QKKXqrippLUjWNAvXiEPc5Fo6G-_H0CPRusrJQ0vb3Tf2iWyj6wKd7LaWRuzgIwRaq0iyWXhWJPlYIfB120h3gokRyc-MHCEPV8xza2dY7jLqL0dglEy6M5lT9YDlSUcbpF7F8YjgiCEjQEQR8SB7a2KvAECsTyQpgsHCB1eyt3zV7IX42kxY4_ijI/s1200/image10.png)

Given the nature of the data structure, the corresponding

cell map walk

involves dereferencing three nested arrays based on the subsequent 1, 10 and 9-bit parts of the cell index, and then adding the final 12-bit offset to the page-aligned address of the target block. The internal kernel structures matching the respective layers of the cell map are \_DUAL, \_HMAP\_DIRECTORY, \_HMAP\_TABLE and \_HMAP\_ENTRY, all publicly accessible via the ntoskrnl.exe PDB symbols. The entry point to the cell map is the Storage array at the end of the \_HHIVE structure:

0:



kd>



dt



\_HHIVE

nt!\_HHIVE

[...]

+0x118



Storage



:



[2]



\_DUAL

The index into the two-element array represents the storage type, 0 for stable and 1 for volatile, so a single \_DUAL structure describes a 2 GiB view of a specific storage space:

0:



kd>



dt



\_DUAL

nt!\_DUAL

+0x000



Length



:



Uint4B

+0x008



Map



:



Ptr64



\_HMAP\_DIRECTORY

+0x010



SmallDir



:



Ptr64



\_HMAP\_TABLE

+0x018



Guard



:



Uint4B

+0x020



FreeDisplay



:



[24]



\_FREE\_DISPLAY

+0x260



FreeBins



:



\_LIST\_ENTRY

+0x270



FreeSummary



:



Uint4B

Let's examine the semantics of each field:

* Length:

  Expresses the current length of the given storage space in bytes. Directly after loading the hive, the stable length is equal to the size of the hive on disk (including any data recovered from log files, minus the 4096 bytes of the header), and the volatile space is empty by definition. Only cell map entries within the [0, Length - 1] range are guaranteed to be valid.
* Map:

  Points to the actual directory structure represented by \_HMAP\_DIRECTORY.
* SmallDir:

  Part of the "small dir" optimization, discussed in the next section.
* Guard:

  Its specific role is unclear, as the field is always initialized to 0xFFFFFFFF upon allocation and never used afterwards. I expect that it is some kind of debugging remnant from the early days of the registry development, presumably related to the small dir optimization.
* FreeDisplay:

  A data structure used to optimize searches for free cells during the cell allocation process. It consists of 24 buckets, each corresponding to a specific cell size range and represented by the \_FREE\_DISPLAY structure, indicating which pages in the hive may potentially contain free cells of the given length.
* FreeBins:

  The head of a doubly-linked list that links the descriptors of entirely empty bins in the hive, represented by the \_FREE\_HBIN structures.
* FreeSummary:

  A bitmask indicating which buckets within FreeDisplay have any hints set for the given cell size. A zero bit at a given position means that there are no free cells of the specific size range anywhere in the hive.

The next level in the cell map hierarchy is the \_HMAP\_DIRECTORY structure:

0:



kd>



dt



\_HMAP\_DIRECTORY

nt!\_HMAP\_DIRECTORY

+0x000



Directory



:



[1024]



Ptr64



\_HMAP\_TABLE

As we can see, it is simply a 1024-element array of pointers to \_HMAP\_TABLE:

0:



kd>



dt



\_HMAP\_TABLE

nt!\_HMAP\_TABLE

+0x000



Table



:



[512]



\_HMAP\_ENTRY

Further, we get a 512-element array of pointers to the final level of the cell map, \_HMAP\_ENTRY:

0:



kd>



dt



\_HMAP\_ENTRY

nt!\_HMAP\_ENTRY

+0x000



BlockOffset



:



Uint8B

+0x008



PermanentBinAddress



:



Uint8B

+0x010



MemAlloc



:



Uint4B

This last level contains a descriptor of a single page in the hive and warrants a deeper analysis. Let's start by noting that the four least significant bits of PermanentBinAddress correspond to a set of undocumented flags that control various aspects of the page behavior. I was able to reverse-engineer them and partially recover their names, largely thanks to the fact that some older Windows 10 builds contained non-inlined functions operating on these flags, with revealing names like HvpMapEntryIsDiscardable or HvpMapEntryIsTrimmed:

enum

\_MAP\_ENTRY\_FLAGS

{

MAP\_ENTRY\_NEW\_ALLOC



=



0x1

,

MAP\_ENTRY\_DISCARDABLE



=



0x2

,

MAP\_ENTRY\_TRIMMED



=



0x4

,

MAP\_ENTRY\_DUMMY



=



0x8

,

};

Here's a brief summary of their meaning based on my understanding:

* MAP\_ENTRY\_NEW\_ALLOC:

  Indicates that this is the first page of a bin. Cell indexes pointing into this page must specify an offset within the range of [0x20, 0xFFF], as they cannot fall into the first 32 bytes that correspond to the \_HBIN structure.
* MAP\_ENTRY\_DISCARDABLE:

  Indicates that the whole bin is empty and consists of a single free cell.
* MAP\_ENTRY\_TRIMMED:

  Indicates that the page has been marked as "trimmed" in HvTrimHive. More specifically, this property is related to hive reorganization, and is set during the loading process on some number of trailing pages that only contain keys accessed during boot, or not accessed at all since the last reorganization. The overarching goal is likely to prevent introducing unnecessary fragmentation in the hive by avoiding mixing together keys with different access histories.
* MAP\_ENTRY\_DUMMY:

  Indicates that the page is allocated from the kernel pool and isn't part of a section view.

With this in mind, let's dive into the details of each \_HMAP\_ENTRY structure member:

* PermanentBinAddress:

  The lower 4 bits contain the above flags. The upper 60 bits represent the base address of the bin mapping corresponding to this page.
* BlockOffset:

  This field has a dual functionality. If the MAP\_ENTRY\_DISCARDABLE flag is set, it is a pointer to a descriptor of a free bin, \_FREE\_HBIN, linked into the \_DUAL.FreeBins linked list. If it is clear (the typical case), it expresses the offset of the page relative to the start of the bin. Therefore, the virtual address of the block's data in memory can be calculated as (PermanentBinAddress & (~0xF)) + BlockOffset.
* MemAlloc:

  If the MAP\_ENTRY\_NEW\_ALLOC flag is set, it contains the size of the bin, otherwise it is zero.

And this concludes the description of how cell maps are structured. Taking all of it into account, the implementation of the HvpGetCellPaged function starts to make a lot of sense. Its pseudocode comes down to the following:

\_CELL\_DATA



\*HvpGetCellPaged(\_HHIVE



\*Hive,



HCELL\_INDEX



Index)



{

\_HMAP\_ENTRY



\*Entry



=



&Hive->Storage[Index



>>



31

].Map

->Directory[(Index



>>



21

)



&



0x3FF

]

->Table[(Index



>>



12

)



&



0x1FF

];

return



(Entry->PermanentBinAddress



&



(~

0xF

))



+



Entry->BlockOffset



+



(Index



&



0xFFF

)



+



4

;

}

The same process is followed, for example, by the implementation of the WinDbg !reg cellindex extension, which also translates a pair of a hive pointer and a cell index into the virtual address of the cell.

##### The small dir optimization

There is one other implementation detail about the cell maps worth mentioning here – the small dir optimization. Let's start with the observation that a majority of registry hives in Windows are relatively small, below 2 MiB in size. This can be easily verified by using the !reg hivelist command in WinDbg, and taking note of the values in the "Stable Length" and "Volatile Length" columns. Most of them usually contain values between several kilobytes to hundreds of kilobytes. This would mean that if the kernel allocated the full first-level directory for these hives (taking up 1024 entries × 8 bytes = 8 KiB on 64-bit platforms), they would still only use the first element in it, leading to a non-trivial waste of memory – especially in the context of the early 1990's when the registry was first implemented. In order to optimize this common scenario, Windows developers employed an unconventional approach to simulate a 1-item long "array" with the SmallDir member of type \_HMAP\_TABLE in the \_DUAL structure, and have the \_DUAL.Map pointer point at it instead of a separate pool allocation when possible. Later, whenever the hive grows and requires more than one element of the cell map directory, the kernel falls back to the standard behavior and performs a normal pool allocation for the directory array.

A revised diagram illustrating the cell map layout of a small hive is shown below:

[![Diagram illustrating the Windows Registry cell index structure and lookup process with the "small dir" optimization applied for small hives. It shows the Cell index fields (Storage selector, Directory index, Table index, Byte offset). The Directory index points to a "Small directory" structure, visually indicating that although the index allows for 1024 entries, only the first entry is typically represented by the embedded structure in this optimized scenario to save memory, with the rest marked as unused initially. The lookup proceeds via Storage list, Small directory, and Table to locate the target Cell block.](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjb62kYOUriRjh1B1hzYJFnWCpLi69AEJ0QoqVBlVSlifW4Wjdyg0w-kQCPdsqlpSPtiSv1YfG137ej2Cl3RxY0B45XPcrNWWnsbFUvbNd9aE5tJ32_pYcKK3gq72fdZeO5PLnOHaLbj-rJCfWMwpYyh424tfQ30HsIrluDkS0xTd0haV-xZMTB8i4XVlQ/s1200/image2.png "Diagram illustrating the Windows Registry cell index structure and lookup process with the \"small dir\" optimization applied for small hives. It shows the Cell index fields (Storage selector, Directory index, Table index, Byte offset). The Directory index points to a \"Small directory\" structure, visually indicating that although the index allows for 1024 entries, only the first entry is typically represented by the embedded structure in this optimized scenario to save memory, with the rest marked as unused initially. The lookup proceeds via Storage list, Small directory, and Table to locate the target Cell block.")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjb62kYOUriRjh1B1hzYJFnWCpLi69AEJ0QoqVBlVSlifW4Wjdyg0w-kQCPdsqlpSPtiSv1YfG137ej2Cl3RxY0B45XPcrNWWnsbFUvbNd9aE5tJ32_pYcKK3gq72fdZeO5PLnOHaLbj-rJCfWMwpYyh424tfQ30HsIrluDkS0xTd0haV-xZMTB8i4XVlQ/s1200/image2.png)

Here, we can see that indexes 1 through 1023 of the directory array are invalid. Instead of correctly initialized \_HMAP\_TABLE structures, they point into "random" data corresponding to other members of the \_DUAL and the larger \_CMHIVE structure that happen to be located after \_DUAL.SmallDir. Ordinarily, this is merely a low-level detail that doesn't have any meaningful implications, as all actively loaded hives remain internally consistent and always contain cell indexes that remain within the bounds of the hive's storage space. However, if we look at it through the security lens of hive-based memory corruption, this behavior suddenly becomes very interesting. If an attacker was able to implant an out-of-bounds cell index with the directory index greater than 0 into a hive, they would be able to get the kernel to operate on invalid (but deterministic) data as part of the cell map walk, and enable a powerful arbitrary read/write primitive. In addition to the small dir optimization, this technique is also enabled by the fact that the HvpGetCellPaged routine doesn't perform any bounds checks of the cell indexes, instead blindly trusting that they are always valid.

If you are curious to learn more about the exploitation aspect of out-of-bounds cell indexes, it was the main subject of my

[Practical Exploitation of Registry Vulnerabilities in the Windows Kernel](https://j00ru.vexillium.org/talks/offensivecon-practical-exploitation-of-windows-registry-vulnerabilities/)

talk given at OffensiveCon 2024 (slides and video recording are available). I will also discuss it in more detail in one of the future blog posts focused specifically on the security impact of registry vulnerabilities.

### \_CMHIVE structure overview

Beyond the first member of type \_HHIVE at offset 0, the \_CMHIVE structure contains more than 3 KiB of further information describing an active hive. This data relates to concepts more abstract than memory management, such as the registry tree structure itself. Below, instead of a field-by-field analysis, we'll focus on the general categories of information within \_CMHIVE, organized loosely by increasing complexity of the data structures:

* Reference count:

  a 32-bit refcount primarily used during short-term operations on the hive, to prevent the object from being freed while actively operated on. These are used by the thin wrappers CmpReferenceHive and CmpDereferenceHive.
* File handles and sizes:

  handles and current sizes of the hive files on disk, such as the main hive file (.DAT) and the accompanying log files (.LOG, .LOG1, .LOG2). The handles are stored in FileHandles array, and the sizes reside in ActualFileSize and LogFileSizes.
* Text strings:

  some informational strings that may prove useful when trying to identify a hive based on its \_CMHIVE structure. For example, the hive file name is stored in FileUserName, and the hive mount point path is stored in HiveRootPath.
* Timestamps:

  there are several timestamps that can be found in the hive descriptor, such as DirtyTime, UnreconciledTime or LastWriteTime.
* List entries:

  instances of the \_LIST\_ENTRY structure used to link the hive into various double-linked lists, such as the global list of hives in the system (HiveList, starting at nt!CmpHiveListHead), or the list of hives within a common trust class (TrustClassEntry).
* Synchronization mechanisms:

  various objects used to synchronize access to the hive as a whole, or some of its parts. Examples include HiveRundown, SecurityLock and HandleClosePendingEvent.
* Unload history:

  a 128-element array that stores the number of steps that have been successfully completed in the process of unloading the hive. Its specific purpose is unclear, it might be a debugging artifact retained from older versions of Windows.
* Late unload state:

  objects related to deferred unloading of registry hives (LateUnloadWorkItemState, LateUnloadFinishedEvent, LateUnloadWorkItem).
* Hive layout information:

  the hive reorganization process in Windows tries to optimize hives by grouping together keys accessed during system runtime, followed by keys accessed during system boot,

  followed by completely unused keys

  . If a hive is structured according to this order during load, the kernel saves information about the boundaries between the three distinct areas in the BootStart, UnaccessedStart and UnaccessedEnd members of \_CMHIVE.
* Flushing state and dirty block information:

  any state that has to do with marking cells as dirty and synchronizing their contents to disk. There are a significant number of fields related to the functionality, with names starting with "Flush...", "Unreconciled..." and "CapturedUnreconciled...".
* Volume context:

  a pointer to a public \_CMP\_VOLUME\_CONTEXT structure, which provides extended information about the disk volume of the hive file. As an example, it is used in the internal CmpVolumeContextMustHiveFilePagesBeKeptLocal routine to determine whether the volume is a system one, and consequently whether certain security/reliability assumptions are guaranteed for it or not.
* KCB table and root KCB:

  a table of the globally visible KCB (Key Control Block) structures corresponding to keys in the hive, and a pointer to the root key's KCB. I will discuss KCBs in more detail in the "Key structures" section below.
* Security descriptor cache:

  a cache of all security descriptors present in the hive, allocated from the kernel pool and thus accessible more efficiently than the underlying hive mappings. In my bug reports, I have often taken advantage of the security cache as a straightforward way to demonstrate the exploitability of security descriptor use-after-frees. A security node UAF can be easily converted into an UAF of its pool-based cached object, which then reliably triggers a Blue Screen of Death when Special Pool is enabled. The security cache of any given hive can be enumerated using the !reg seccache command in WinDbg.
* Transaction-related objects:

  a pointer to a \_CM\_RM structure that describes the Resource Manager object associated with the hive, if "heavyweight" transactions (i.e. KTM transactions) are enabled for it.

Last but not least,

\_CMHIVE has its own Flags field that is different from \_HHIVE.Flags

. As usual, the flags are not documented, so the listing below is a product of my own analysis:

enum



\_CM\_HIVE\_FLAGS

{

CM\_HIVE\_UNTRUSTED



=



0x1

,

CM\_HIVE\_IN\_SID\_MAPPING\_TABLE



=



0x2

,

CM\_HIVE\_HAS\_RM



=



0x8

,

CM\_HIVE\_IS\_VIRTUALIZABLE



=



0x10

,

CM\_HIVE\_APP\_HIVE



=



0x20

,

CM\_HIVE\_PROCESS\_PRIVATE



=



0x40

,

CM\_HIVE\_MUST\_BE\_REORGANIZED



=



0x400

,

CM\_HIVE\_DIFFERENCING\_WRITETHROUGH



=



0x2000

,

CM\_HIVE\_CLOUDFILTER\_PROTECTED



=



0x10000

,

};

A brief description of each of them is as follows:

* CM\_HIVE\_UNTRUSTED:

  the hive is "untrusted" in the sense of registry symbolic links; in other words, it is not one of the default system hives loaded on boot. The distinction is that trusted hives can freely link to all other hives in the system, while untrusted ones can only link to hives within their so-called trust class. This is to prevent confused deputy-style privilege escalation attacks in the system.
* CM\_HIVE\_IN\_SID\_MAPPING\_TABLE:

  the hive is linked into an internal data structure called the "SID mapping table" (nt!CmpSIDToHiveMapping), used to efficiently look up the user class hives mounted at \Registry\User\<SID>\_Classes for the purposes of registry virtualization.
* CM\_HIVE\_HAS\_RM:

  KTM transactions are enabled for this hive, meaning that the corresponding .blf and .regtrans-ms files are present in the same directory as the main hive file. The flag is clear if the hive is an app hive or if it was loaded with the REG\_HIVE\_NO\_RM flag set.
* CM\_HIVE\_IS\_VIRTUALIZABLE:

  accesses to this hive may be subject to registry virtualization. As far as I know, the only hive with this flag set is currently HKLM\SOFTWARE, which seems in line with the official

  [documentation](https://learn.microsoft.com/en-us/windows/win32/sysinfo/registry-virtualization#registry-virtualization-scope)

  .
* CM\_HIVE\_APP\_HIVE:

  this is an app hive, i.e. it was loaded under \Registry\A with the REG\_APP\_HIVE flag set.
* CM\_HIVE\_PROCESS\_PRIVATE:

  this hive is private to the loading process, i.e. it was loaded with the REG\_PROCESS\_PRIVATE flag set.
* CM\_HIVE\_MUST\_BE\_REORGANIZED:

  the hive fragmentation threshold (by default 1 MiB) has been exceeded, and the hive should undergo the reorganization process at the next opportunity. The flag is simply a means of communication between the CmCheckRegistry and CmpReorganizeHive internal routines, both of which execute during hive loading.
* CM\_HIVE\_DIFFERENCING\_WRITETHROUGH:

  this is a delta hive loaded in the writethrough mode, which technically means that the DIFF\_HIVE\_WRITETHROUGH flag was specified in the DiffHiveFlags member of the VRP\_LOAD\_DIFFERENCING\_HIVE\_INPUT structure, as discussed in

  [Part 4](https://googleprojectzero.blogspot.com/2024/10/the-windows-registry-adventure-4-hives.html)

  .
* CM\_HIVE\_CLOUDFILTER\_PROTECTED:

  new flag added in December 2024 as part of the fix for

  [CVE-2024-49114](https://project-zero.issues.chromium.org/issues/42451734)

  . It indicates that the hive file has been protected against being converted to a

  [Cloud Filter](https://learn.microsoft.com/en-us/windows/win32/api/_cloudapi/)

  placeholder by setting the "$Kernel.CFDoNotConvert" extended attribute (EA) on the file in CmpAdjustFileCFSafety.

This concludes the documentation of the hive descriptor structure, arguably the largest and most complex object in the Windows registry implementation.

## Key structures

The second most important objects in the registry are keys. They can be basically thought of as the essence of the registry, as nearly every registry operation involves them in some way. They are also the one and only registry element that is tightly integrated with the Windows NT Object Manager. This comes with many benefits, as client applications can operate on the registry using standardized

handles, and can leverage automatic security checks and object lifetime management. However, this integration also presents its own challenges, as it requires the Configuration Manager to interact with the Object Manager correctly and handle its intricacies and edge cases securely. For this reason, internal key-related structures play a crucial role in the registry implementation. They help organize key

state

in a way that simplifies keeping it up-to-date and internally consistent. For security researchers, understanding these structures and their semantics is invaluable. This knowledge enables you to quickly identify bugs in existing code or uncover missing handling of unusual but realistic conditions.

The two fundamental key structures in the Windows kernel are the

key body

(\_CM\_KEY\_BODY) and

key control block

(\_CM\_KEY\_CONTROL\_BLOCK)

. The key body is directly associated with a key handle in the NT Object Manager, similar to the role that the \_FILE\_OBJECT structure plays for file handles. In other words, this is the initial object that the kernel obtains whenever it calls ObReferenceObjectByHandle to reference a user-supplied handle. There may concurrently exist a number of key body structures associated with a single key, as long as there are several programs holding active handles to the key. Conversely, the key control block represents the global state of a specific key and is used to manage its general properties. This means that for most keys in the system, there is at most one KCB allocated at a time. There may be no KCB for keys that haven't been accessed yet (as they are initialized by the kernel lazily), and there may be more than one KCB for the same registry path if the key has been deleted and created again (these two instances of the key are treated as separate entities, with one of them being marked as deleted/non-existent). Taking this into account, the relationship between key bodies and KCBs is many-to-one, with all of the key bodies of a single KCB being connected in a doubly-linked list, as shown in the diagram below:

[![Diagram illustrating the many-to-one relationship between Windows Registry Key Bodies and a Key Control Block (KCB). A single KCB is shown linked to multiple Key Body structures. These Key Bodies are themselves connected together in a doubly-linked list, which is associated with the parent KCB.](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhVOPG2OhtTCa9UQCPsoHCURy3PQqp9yTFutGDPMiP1uPhb1nTMdAzzeAKPPkDunbzqrGSo2pp0N-fC_cBBdXzGjF22FLgTyV_gLz6w92npQlxpdtd4RB5aWAdrx9tn7hcl6fIAqm5uP6eoSIY_OWC4cXiPVjh3_VFmhyphenhyphenqwCGUnurBCLbL0Qwj-eKHMCLA/s1200/image4.png "Diagram illustrating the many-to-one relationship between Windows Registry Key Bodies and a Key Control Block (KCB). A single KCB is shown linked to multiple Key Body structures. These Key Bodies are themselves connected together in a doubly-linked list, which is associated with the parent KCB.")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhVOPG2OhtTCa9UQCPsoHCURy3PQqp9yTFutGDPMiP1uPhb1nTMdAzzeAKPPkDunbzqrGSo2pp0N-fC_cBBdXzGjF22FLgTyV_gLz6w92npQlxpdtd4RB5aWAdrx9tn7hcl6fIAqm5uP6eoSIY_OWC4cXiPVjh3_VFmhyphenhyphenqwCGUnurBCLbL0Qwj-eKHMCLA/s1200/image4.png)

The following subsections provide more detail about each of these two structures.

### Key body

The key body structure is allocated and initialized in the internal CmpCreateKeyBody routine, and freed by the NT Object Manager when all references to the object are dropped. It is a relatively short and simple object with the following definition:

0:



kd>



dt



\_CM\_KEY\_BODY

nt!\_CM\_KEY\_BODY

+0x000



Type



:



Uint4B

+0x004



AccessCheckedLayerHeight



:



Uint2B

+0x008



KeyControlBlock



:



Ptr64



\_CM\_KEY\_CONTROL\_BLOCK

+0x010



NotifyBlock



:



Ptr64



\_CM\_NOTIFY\_BLOCK

+0x018



ProcessID



:



Ptr64



Void

+0x020



KeyBodyList



:



\_LIST\_ENTRY

+0x030



Flags



:



Pos



0,



16



Bits

+0x030



HandleTags



:



Pos



16,



16



Bits

+0x038



Trans



:



\_CM\_TRANS\_PTR

+0x040



KtmUow



:



Ptr64



\_GUID

+0x048



ContextListHead



:



\_LIST\_ENTRY

+0x058



EnumerationResumeContext



:



Ptr64



Void

+0x060



RestrictedAccessMask



:



Uint4B

+0x064



LastSearchedIndex



:



Uint4B

+0x068



LockedMemoryMdls



:



Ptr64



Void

Let's quickly go over each field:

* Type:

  for normal keys (i.e. almost all of them), this field is set to a magic value of 0x6B793032 ('ky02'). However, for predefined keys, this is the 32-bit value of the link's target key with the highest bit set. This member is therefore used to distinguish between regular keys and predefined ones, for example in CmObReferenceObjectByHandle. Predefined keys have been now largely deprecated, but it is still possible to observe a non-standard Type value by opening a handle to one of the two last remaining ones: HKLM\Software\Microsoft\Windows NT\CurrentVersion\Perflib\009 and CurrentLanguage under the same path.
* AccessCheckedLayerHeight:

  a new field added in November 2023 as part of the fix for

  [CVE-2023-36404](https://project-zero.issues.chromium.org/issues/42451625)

  . It is used for layered keys and contains the index of the lowest layer in the key stack that was access-checked when opening the key. It is later taken into account during other registry operations, in order to avoid leaking data from lower-layer, more restrictive keys that could have been created since the handle was opened.
* KeyControlBlock:

  a pointer to the corresponding key control block.
* NotifyBlock:

  an optional pointer to the notify block associated with this handle. This is related to the

  [key notification functionality](https://learn.microsoft.com/en-us/windows/win32/api/winreg/nf-winreg-regnotifychangekeyvalue)

  in Windows and is described in more detail in the "Key notification structures" section below.
* ProcessID:

  the PID of the process that created the handle. It doesn't seem to serve any purpose in the kernel other than to be enumerable using the NtQueryOpenSubKeysEx system call (which requires SeRestorePrivilege, and is therefore available to administrators only).
* KeyBodyList:

  the list entry used to link all the key bodies within a single KCB together.
* Flags:

  a set of flags concerning the specific key body. Here's my interpretation of them based on reverse engineering:

* KEY\_BODY\_HIVE\_UNLOADED (0x1): indicates that the underlying hive of the key has been unloaded and is no longer active.
* KEY\_BODY\_DONT\_RELOCK (0x2): this seems to be a short-term flag used to communicate between CmpCheckKeyBodyAccess/CmpCheckOpenAccessOnKeyBody and the nested CmpDoQueryKeyName routine, in order to indicate that the key's KCB is already locked and shouldn't be relocked again.
* KEY\_BODY\_DONT\_DEINIT (0x4): if this flag is set, CmpDeleteKeyObject returns early and doesn't proceed with the regular deinitialization of the key body object. However, it is unclear if/where the flag is set in the code, as I personally haven't found any instances of it happening during my analysis.
* KEY\_BODY\_DELETED (0x8): indicates that the key has been deleted since the handle was opened, and it no longer exists.
* KEY\_BODY\_DONT\_VIRTUALIZE (0x10): indicates that registry virtualization is disabled for this handle, as a result of opening the key with the (undocumented but present in SDK headers) REG\_OPTION\_DONT\_VIRTUALIZE flag.

* HandleTags:

  from the kernel perspective, this is simply a general purpose 16-bit storage that can be set by clients on a per-handle basis using NtSetInformationKey with the KeySetHandleTagsInformation information class, and queried with NtQueryKey and the KeyHandleTagsInformation information class. As far as I know, the kernel doesn't dictate how this field should be used and leaves it up to the registry clients. In practice, it seems to be mostly used for purposes related to WOW64 and the

  [Registry Redirector](https://learn.microsoft.com/en-us/windows/win32/winprog64/registry-redirector)

  , storing flags such as KEY\_WOW64\_64KEY (0x100) and KEY\_WOW64\_32KEY (0x200), as well as some internal ones. The WOW64 functionality is implemented in KernelBase.dll, and functions such as ConstructKernelKeyPath and LocalBaseRegOpenKey are a good starting point for reverse engineering, if you're curious to learn more. I have also observed the 0x1000 handle tag being set in the internal IopApplyMutableTagToRegistryKey kernel routine for keys such as HKLM\System\ControlSet001\Control\Class\{4D36E968-E325-11CE-BFC1-08002BE10318}\0000, but I'm unsure of its meaning.
* Trans:

  Indicates the transactional state of the handle. If the handle is not transacted (i.e. it wasn't opened with one of

  [RegOpenKeyTransacted](https://learn.microsoft.com/en-us/windows/win32/api/winreg/nf-winreg-regopenkeytransactedw)

  or

  [RegCreateKeyTransacted](https://learn.microsoft.com/en-us/windows/win32/api/winreg/nf-winreg-regcreatekeytransactedw)

  ), it is set to zero. Otherwise, the lowest bit specifies the type of the transaction: 0 for KTM and 1 for lightweight transactions. The remaining bits form a pointer to the associated transaction object, either of the TmTransactionObjectType type (represented by the \_KTRANSACTION structure), or of the CmRegistryTransactionType type (represented by a non-public structure that I've personally named \_CM\_LIGHTWEIGHT\_TRANS\_OBJECT).
* KtmUow

  :

  if the handle is associated with a KTM transaction, this field stores the GUID that uniquely identifies it. For non-transacted and lightweight-transacted handles, the field is unused.
* ContextListHead:

  this is the head of the doubly-linked list of contexts that have been associated with the key body using the

  [CmSetCallbackObjectContext](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdm/nf-wdm-cmsetcallbackobjectcontext)

  function. It is related to the

  [registry callbacks](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdm/nf-wdm-cmregistercallbackex)

  functionality; see also the

  [Specifying Context Information](https://learn.microsoft.com/en-us/windows-hardware/drivers/kernel/specifying-context-information)

  MSDN article for more details.
* EnumerationResumeContext:

  this is part of an optimization of the subkey enumeration process of layered keys (implemented in CmpEnumerateLayeredKey). Performing full enumeration of a layered key from scratch up to the given index is a very complex task, and repeating it over and over for each iteration of an enumeration loop would be very inefficient. The resume context helps address the problem for sequential enumeration by saving the intermediate state reached at an NtEnumerateKey call with a given index, and being able to resume from it when a request for index+1 comes next. It also has the added benefit of making it possible to stop and restart the enumeration process in the scope of a single system call, which is used to pause the operation and temporarily release some locks if the code detects that the registry is particularly congested. This happens at the intersection of the CmEnumerateKey and CmpEnumerateLayeredKey functions, with the latter potentially returning STATUS\_RETRY and the former resuming the operation if such a situation arises.
* RestrictedAccessMask, LastSearchedIndex, LockedMemoryMdls:

  relatively new fields introduced in Windows 10 and 11, which I haven't looked very deeply into and thus won't discuss in detail here.

After a key handle is translated into the corresponding \_CM\_KEY\_BODY structure using the ObReferenceObjectByHandle(CmKeyObjectType) call, typically early in the execution of a registry-related system call, there are three primary operations that are usually performed. First, the kernel does a key status check by evaluating the expression

KeyBody.Flags & 9

to determine if the key is associated with an unloaded hive (flag 0x1) or has been deleted (flag 0x8). This check is essential because most registry operations are only permitted on active, existing keys, and enforcing this condition is a fundamental step for guaranteeing registry state consistency. Second, the code accesses the KeyControlBlock pointer, which provides further access to the hive pointer (KCB.KeyHive), the key's cell index (KCB.KeyCell), and other necessary fields and data structures required to perform any meaningful read/write actions on the key. Finally, the code checks the key body's Trans/KtmUow members to determine if the handle is part of a transaction, and if so, the transaction is used as additional context for the action requested by the caller. Accesses to other members of the \_CM\_KEY\_BODY structure are less frequent and serve more specialized purposes.

### Key control block

The key control block object can be thought of as the heart of the Windows kernel registry tree representation. It is effectively

the

descriptor of a single key in the system, and the second most important key-related object after the key node. It is always allocated from the kernel pool, and serves four main purposes:

1. Mirrors frequently used information from the key node to make it faster to access by the kernel code. This includes building an efficient, in-memory representation of the registry tree to optimize the traversal time when referring to registry paths.
2. Works as a single point of reference for all active handles to a specific key, and helps synchronize access to the key in the multithreaded Windows environment.
3. Represents any pending, transacted state of the registry key that has been introduced by a client, but not fully committed yet.
4. Represents any complex relationships between registry keys that extend beyond the internal structure of the hive. The primary example are differencing hives, which are overlaid on top of each other, and whose corresponding keys form so-called

   key stacks

   .

[Blog post #2](https://googleprojectzero.blogspot.com/2024/04/the-windows-registry-adventure-2.html)

in this series highlighted the dramatic growth of the registry codebase across successive Windows versions, illustrating the subsystem's steady expansion over the last few decades. Similarly, the size of the Key Control Block (KCB) itself has nearly doubled in time, from 168 bytes in Windows XP x64 to 312 bytes in the latest Windows 11 release. This expansion underscores the increasing amount of information associated with every registry key, which the kernel must manage consistently and securely.

The KCB structure layout is present in the PDB symbols and can be displayed in WinDbg:

0:



kd>



dt



\_CM\_KEY\_CONTROL\_BLOCK

nt!\_CM\_KEY\_CONTROL\_BLOCK

+0x000



RefCount



:



Uint8B

+0x008



ExtFlags



:



Pos



0,



16



Bits

+0x008



Freed



:



Pos



16,



1



Bit

+0x008



Discarded



:



Pos



17,



1



Bit

+0x008



HiveUnloaded



:



Pos



18,



1



Bit

+0x008



Decommissioned



:



Pos



19,



1



Bit

+0x008



SpareExtFlag



:



Pos



20,



1



Bit

+0x008



TotalLevels



:



Pos



21,



10



Bits

+0x010



KeyHash



:



\_CM\_KEY\_HASH

+0x010



ConvKey



:



\_CM\_PATH\_HASH

+0x018



NextHash



:



Ptr64



\_CM\_KEY\_HASH

+0x020



KeyHive



:



Ptr64



\_HHIVE

+0x028



KeyCell



:



Uint4B

+0x030



KcbPushlock



:



\_EX\_PUSH\_LOCK

+0x038



Owner



:



Ptr64



\_KTHREAD

+0x038



SharedCount



:



Int4B

+0x040



DelayedDeref



:



Pos



0,



1



Bit

+0x040



DelayedClose



:



Pos



1,



1



Bit

+0x040



Parking



:



Pos



2,



1



Bit

+0x041



LayerSemantics



:



UChar

+0x042



LayerHeight



:



Int2B

+0x044



Spare1



:



Uint4B

+0x048



ParentKcb



:



Ptr64



\_CM\_KEY\_CONTROL\_BLOCK

+0x050



NameBlock



:



Ptr64



\_CM\_NAME\_CONTROL\_BLOCK

+0x058



CachedSecurity



:



Ptr64



\_CM\_KEY\_SECURITY\_CACHE

+0x060



ValueList



:



\_CHILD\_LIST

+0x068



LinkTarget



:



Ptr64



\_CM\_KEY\_CONTROL\_BLOCK

+0x070



IndexHint



:



Ptr64



\_CM\_INDEX\_HINT\_BLOCK

+0x070



HashKey



:



Uint4B

+0x070



SubKeyCount



:



Uint4B

+0x078



KeyBodyListHead



:



\_LIST\_ENTRY

+0x078



ClonedListEntry



:



\_LIST\_ENTRY

+0x088



KeyBodyArray



:



[4]



Ptr64



\_CM\_KEY\_BODY

+0x0a8



KcbLastWriteTime



:



\_LARGE\_INTEGER

+0x0b0



KcbMaxNameLen



:



Uint2B

+0x0b2



KcbMaxValueNameLen



:



Uint2B

+0x0b4



KcbMaxValueDataLen



:



Uint4B

+0x0b8



KcbUserFlags



:



Pos



0,



4



Bits

+0x0b8



KcbVirtControlFlags



:



Pos



4,



4



Bits

+0x0b8



KcbDebug



:



Pos



8,



8



Bits

+0x0b8



Flags



:



Pos



16,



16



Bits

+0x0bc



Spare3



:



Uint4B

+0x0c0



LayerInfo



:



Ptr64



\_CM\_KCB\_LAYER\_INFO

+0x0c8



RealKeyName



:



Ptr64



Char

+0x0d0



KCBUoWListHead



:



\_LIST\_ENTRY

+0x0e0



DelayQueueEntry



:



\_LIST\_ENTRY

+0x0e0



Stolen



:



Ptr64



UChar

+0x0f0



TransKCBOwner



:



Ptr64



\_CM\_TRANS

+0x0f8



KCBLock



:



\_CM\_INTENT\_LOCK

+0x108



KeyLock



:



\_CM\_INTENT\_LOCK

+0x118



TransValueCache



:



\_CHILD\_LIST

+0x120



TransValueListOwner



:



Ptr64



\_CM\_TRANS

+0x128



FullKCBName



:



Ptr64



\_UNICODE\_STRING

+0x128



FullKCBNameStale



:



Pos



0,



1



Bit

+0x128



Reserved



:



Pos



1,



63



Bits

+0x130



SequenceNumber



:



Uint8B

I will not document each member individually, but will instead cover them in larger groups according to their common themes and functions.

#### Reference count

Key Control Blocks are among the most frequently referenced registry objects

, as a

lmost every persistent registry operation involves an associated KCB. These blocks are referenced in various ways: by a subkey's KCB.ParentKcb pointer, a symbolic link key's KCB.LinkTarget pointer, through the global KCB tree, via open key handles (and the corresponding key bodies), in pending

transacted

operations (e.g., the \_CM\_KCB\_UOW.KeyControlBlock pointer)

, and so on.

For system stability and security, it's crucial to accurately track all these active KCB references.



This is done using the

RefCount

field, the first member in the KCB structure (offset 0x0).



Historically a 16-bit field, it became a 32-bit integer, and on modern systems, it is a native word size—typically 64-bits on most computers.



Whenever kernel code needs to operate on a KCB or store a pointer to it, it should increment the RefCount using functions from the CmpReferenceKeyControlBlock family.



Conversely, when a KCB reference is no longer needed, functions like CmpDereferenceKeyControlBlock should

decrement

the count.



When RefCount reaches zero, the kernel knows the structure is no longer in use and can safely free it.

Besides standard reference counting, KCBs employ optimizations to delay certain memory management processes.



This avoids excessive KCB allocation and deallocation when a KCB is briefly unreferenced.



Two mechanisms are used:

delay deref

and

delay close

.



The former delays the actual refcount decrement, while the latter postpones object deallocation even after RefCount reaches zero.



Callers must use the specialized function CmpDelayDerefKeyControlBlock for the delayed dereference.

From a low-level security perspective, it's worth considering potential issues related to the reference counting.



Integer overflow might seem like a possibility, but it's practically impossible due to the field's width and additional overflow protection present in the CmpReferenceKeyControlBlock-like functions.



A more realistic concern is a scenario where the kernel accidentally decrements the refcount by a larger value than the number of released references.



This could lead to premature KCB deallocation and a use-after-free condition.



Therefore, accurate KCB reference counting is a crucial area to investigate when researching Windows for registry vulnerabilities.

#### Basic key information

As mentioned earlier, one of the most important types of information in the KCB is the unique identifier of the key in the hive, consisting of the \_HHIVE descriptor pointer (

KeyHive

) and the corresponding key cell index (

KeyCell

). Very frequently, the kernel uses these two members to obtain the address of the key node mapping, which resembles the following pattern in the decompiled code:

\_HHIVE



\*Hive



=



Kcb->KeyHive;

\_CM\_KEY\_NODE



\*KeyNode



=



Hive->GetCellRoutine(Hive,



Kcb->KeyCell);

//

// Further operations on KeyNode...

/

/

#### Cached data from the key node

Whenever some information about a key needs to be queried based on its handle, it is generally more efficient to read it from the KCB than the key node. The reason is that a pool-based KCB access requires fewer memory fetches (it avoids the cell map walk), bypasses the context switch to the Registry process, and eliminates the potential need to page in hive data from disk. Consequently, the following types of information are cached inside KCBs:

* Key name

  , which is stored in a public \_CM\_NAME\_CONTROL\_BLOCK structure and pointed to by the

  NameBlock member

  . Every unique key name in the system has its own instance of the \_CM\_NAME\_CONTROL\_BLOCK object, which is reference-counted and shared across all KCBs of keys with that name. This is an optimization designed to prevent storing multiple redundant copies of the same string in kernel memory.
* Flags

  , stored in the

  Flags

  member and being an exact copy of the \_CM\_KEY\_NODE.Flags value. There is also the KcbUserFlags field that caches the value of \_CM\_KEY\_NODE.UserFlags, and KcbVirtControlFlags, which caches the value of \_CM\_KEY\_NODE.VirtControlFlags. The semantics of all of these bitmasks were discussed in

  [Part 5](https://googleprojectzero.blogspot.com/2024/12/the-windows-registry-adventure-5-regf.html)

  .
* Security descriptor

  , stored in a separate \_CM\_KEY\_SECURITY\_CACHE structure and pointed to by

  CachedSecurity

  .
* Subkey count

  , stored in the SubKeyCount field. It expresses the cumulative number of the key's stable and volatile subkeys, i.e. it is equal to the sum of \_CM\_KEY\_NODE.SubKeyCounts[0] and SubKeyCounts[1].
* Value list

  , stored in the ValueList structure of type \_CHILD\_LIST, and equivalent to \_CM\_KEY\_NODE.ValueList.
* Key limits

  , represented by KcbMaxNameLen, KcbMaxValueNameLen and KcbMaxValueDataLen. They correspond to the key node fields with the same names without the "Kcb" prefix.
* Fully qualified path

  , stored in FullKCBName. It is lazily initialized in the internal CmpConstructAndCacheName function, either when resolving a symbolic link, or as a result of calling the documented

  [CmCallbackGetKeyObjectID](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdm/nf-wdm-cmcallbackgetkeyobjectid)

  API. A previously initialized path may be marked as stale by setting FullKCBNameStale (the least significant bit of the FullKCBName pointer).

It is essential for system security that the information found in KCBs is always synchronized with their key node counterparts. This is one of the most fundamental assumptions of the Windows registry implementation, and failure to guarantee it typically results in memory corruption or other severe security vulnerabilities.

#### Extended flags

In addition to the flags fields that simply mirror the corresponding values from the key node, like Flags, KcbUserFlags and KcbVirtControlFlags, there is also a set of extended flags that are KCB-specific. They are stored in the following fields:

+0x008



ExtFlags



:



Pos



0,



16



Bits

+0x008



Freed



:



Pos



16,



1



Bit

+0x008



Discarded



:



Pos



17,



1



Bit

+0x008



HiveUnloaded



:



Pos



18,



1



Bit

+0x008



Decommissioned



:



Pos



19,



1



Bit

+0x008



SpareExtFlag



:



Pos



20,



1



Bit

[...]

+0x040 DelayedDeref     : Pos 0, 1 Bit

+0x040 DelayedClose     : Pos 1, 1 Bit

+0x040 Parking          : Pos 2, 1 Bit

For the eight explicitly defined flags

, here's a brief explanation:

* Freed:

  the KCB has been freed, but the underlying pool allocation may still be alive as part of the CmpFreeKCBListHead (older systems) or CmpKcbLookaside (Windows 10 and 11) lookaside lists.
* Discarded:

  the KCB has been unlinked from the global KCB tree and is not available for name-based lookups, but there may still be active references to it via open handles. It is typically set for keys that have been deleted, and for old instances of keys that have been renamed.
* HiveUnloaded:

  the underlying hive has been unloaded.
* Decommissioned:

  the KCB is no longer used (its reference count dropped to zero) and it is ready to be freed, but it hasn't been freed just yet.
* SpareExtFlag:

  as the name suggests, this is a spare bit that may be associated with a new flag in the future.
* DelayedDeref:

  the key is subject to a "delayed deref" mechanism, due to having been dereferenced using CmpDelayDerefKeyControlBlock instead of CmpDereferenceKeyControlBlock. This serves to defer the actual dereferencing of the KCB by some time, anticipating its near-future need and thus avoiding a redundant free-allocate sequence.
* DelayedClose:

  the key is subject to a "delayed close" mechanism, which is similar to

  delayed deref

  , but it involves delaying the freeing of a KCB structure even if its refcount has dropped to zero.
* Parking:

  the purpose of this bit is unclear, and it seems to be currently unused.

Last but not least, the ExtFlags member stores a further set of flags, which can be expressed as the following enum:

enum



\_CM\_KCB\_EXT\_FLAGS

{

CM\_KCB\_NO\_SUBKEY



=



0x1

,

CM\_KCB\_SUBKEY\_ONE



=



0x2

,

CM\_KCB\_SUBKEY\_HINT



=



0x4

,

CM\_KCB\_SYM\_LINK\_FOUND



=



0x8

,

CM\_KCB\_KEY\_NON\_EXIST



=



0x10

,

CM\_KCB\_NO\_DELAY\_CLOSE



=



0x20

,

CM\_KCB\_INVALID\_CACHED\_INFO



=



0x40

,

CM\_KCB\_READ\_ONLY\_KEY



=



0x80

,

CM\_KCB\_READ\_ONLY\_SUBKEY    =

0x100

,

};

Let's break it down:

* CM\_KCB\_NO\_SUBKEY

  ,

  CM\_KCB\_SUBKEY\_ONE

  ,

  CM\_KCB\_SUBKEY\_HINT:

  these flags are currently obsolete, and were originally related to an old performance optimization. CM\_KCB\_NO\_SUBKEY indicated that the key had no subkeys. CM\_KCB\_SUBKEY\_ONE indicated that the key had exactly one subkey, and its 32-bit hint value was stored in KCB.HashKey. Finally, CM\_KCB\_SUBKEY\_HINT indicated that the hints of all subkeys were stored in a dynamically allocated buffer pointed to by KCB.IndexHint. According to my analysis, none of the flags seem to be used in modern versions of Windows, even though their related fields in the KCB structure still exist.
* CM\_KCB\_SYM\_LINK\_FOUND:

  indicates that the key is a symbolic link whose target KCB has already been resolved during a previous access, and is cached in KCB.CachedChildList.RealKcb (older systems) or KCB.LinkTarget (Windows 10 and 11). It is an optimization designed to speed up the process of traversing symlinks, by performing the path lookup only once and later referring directly to the cached KCB where possible.
* CM\_KCB\_KEY\_NON\_EXIST:

  this is another deprecated flag that existed in historical implementations of the registry, but doesn't seem to be used anymore.
* CM\_KCB\_NO\_DELAY\_CLOSE:

  indicates that the key mustn't be subject to the "delayed close" mechanism, and instead should be freed as soon as all references to it are dropped.
* CM\_KCB\_INVALID\_CACHED\_INFO:

  this flag simply indicates that the IndexHint/HashKey/SubKeyCount fields contain out-of-date information that shouldn't be relied on.
* CM\_KCB\_READ\_ONLY\_KEY:

  t

  his key is designated as read-only and, therefore, is not modifiable.

  The flag can be set by using the undocumented NtLockRegistryKey system call, which can only be called from kernel-mode. Shout out to James Forshaw who wrote an

  [interesting post](https://www.tiraniddo.dev/2017/07/locking-your-registry-keys-for-fun-and.html)

  about it on his blog.
* CM\_KCB\_READ\_ONLY\_SUBKEY:

  t

  he exact meaning and usage of the flag is unclear, but it appears to be enabled for keys with at least one descendant subkey marked as read-only.



  Specifically, the internal CmLockKeyForWrite function (the main routine behind NtLockRegistryKey's logic) sets it iteratively for every parent key of the read-only key, up to and including the hive's root.

#### Key body list

To optimize access, the KCB stores the first four key body handles in the KeyBodyArray for fast, lockless access. The KeyBodyListHead field maintains the head of a doubly-linked list for any additional handles.

#### KCB lock

The KcbPushlock member within the KCB structure is a lock used to synchronize access to the key during various registry system calls. This lock is passed to standard kernel pushlock APIs, such as ExAcquirePushLockSharedEx, ExAcquirePushLockExclusiveEx, and ExReleasePushLockEx

#### Transacted state

The key control block is central to managing the transacted state of registry keys, maintaining pending changes in memory before they are committed to the hive. Several fields within the KCB are specifically dedicated to this function:

* KCBUoWListHead:

  This field is a list head that anchors a list of

  Unit of Work (UoW) structures

  . Each UoW represents a specific action taken within a transaction, such as creating, deleting a key or setting or deleting a value. This list allows the system to track all pending transactional operations related to a particular key, and it is crucial for ensuring atomicity, as it records the operations that must be applied or rolled back as a single unit.
* TransKCBOwner:

  This field is used to identify the transaction object that "owns" the key. It is set on the KCBs of transactionally created keys, and signifies that the key is currently only visible in the context of the specific transaction. Once the transaction commits, this field is cleared, and the key becomes visible in the global registry tree.
* KCBLock

  and

  KeyLock:

  Two so-called intent locks of type \_CM\_INTENT\_LOCK, which are used to ensure that no two transactions can be associated with a single key if their respective operations could invalidate each other's state. According to my understanding, KCBLock protects the consistency of the KCB in this regard, and KeyLock protects the key node. The !reg ixlock WinDbg command is designed to display the internal state of these locks.
* TransValueCache:

  This field is a structure that caches value entries associated with a particular KCB, if at least one of its values has been modified in an active transaction. Before a value is set, modified or deleted within a transaction for the first time, a copy of the current value list is taken and stored here. When a transaction is committed, the TransValueCache state is applied back to the key's persistent value list. On rollback, the list is simply discarded.
* TransValueListOwner:

  This field is a pointer to a transaction that currently "owns" the TransValueCache. At any given time, for each key, there may be at most one active transaction that has any pending operations involving the key's values.

These fields collectively form the core transaction management within the Windows Registry. Ever since their introduction in Windows Vista, they need to be correctly handled as part of every registry action, be it a read/write one, a transacted/non-transacted one etc. This is because the kernel must potentially incorporate any transacted state in any information queries, and must similarly pay attention not to allow the existence of two contradictory transactions at the same time, and not to allow a non-transacted operation to break any assumptions of an active transaction without invalidating it first. And any bugs related to managing the transacted state may have significant security implications, with some interesting examples being

[CVE-2023-21748](https://project-zero.issues.chromium.org/issues/42451527)

and

[CVE-2023-23420](https://project-zero.issues.chromium.org/issues/42451531)

. The specific structures used to store the transacted state, such as \_CM\_TRANS or \_CM\_KCB\_UOW, are discussed in more detail in the "Transaction structures" section below.

#### Layered key state

Layered keys were introduced in Windows 10 version 1607 to support containerisation through differencing hives. Because overlaying hives on top of each other is primarily a runtime concept, the Key Control Block (KCB) is the natural place to hold the state related to this feature, and there are three main members involved in this process:

* LayerSemantics:

  This 2-bit field indicates the state of a key within the layering system. It is an exact copy of the key's \_CM\_KEY\_NODE.LayerSemantics value, cached in KCB for easier/quicker access. For a detailed overview of its possible values, please refer to

  [Part 5](https://googleprojectzero.blogspot.com/2024/12/the-windows-registry-adventure-5-regf.html)

  .
* LayerHeight:

  This field specifies the level of the key within the differencing hive stack. A higher LayerHeight indicates that the key is higher up in the stack of layered hives, and a value of zero is used for

  base hives

  (i.e. normal non-differencing hives loaded on the host system).
* LayerInfo:

  This is a pointer to a \_CM\_KCB\_LAYER\_INFO structure, which describes the key's position within the stack of differencing hives. Among other things, it contains a pointer to the lower layer on the key stack, and the head of a list of layers above the current one.

The specifics of the structures associated with this functionality are discussed in the "Layered keys" section below.

#### KCB tree structure

While key bodies are a common way to access KCB structures, they're not the only method.

They

are integral when you have an open handle to a key, as operations on the handle follow the handle → key body → KCB translation path.



However, looking up keys by name or path is also crucial.



Whether a key is opened or created, it relies on either an existing handle and a relative path (single subkey name or a longer path with backslash-separated names), or an absolute path starting with "\Registry\".



In this scenario, the kernel needs to quickly check if a KCB exists for the given key and to obtain its address if it does.



To achieve this, KCBs are organized into their own tree structure, which the kernel can traverse.

The

tree is rooted in CmpRegistryRootObject (specifically CmpRegistryRootObject->KeyControlBlock, as CmpRegistryRootObject itself is the key body representing the \Registry key), and mirrors the current registry layout from a high-level perspective

.

[![Diagram illustrating the Windows Registry Key Control Block (KCB) tree structure used for key lookups by name or path. The tree starts with the REGISTRY root, branching into top-level keys like MACHINE and USER. It further details the hierarchy under MACHINE, showing SOFTWARE linked to another SOFTWARE node which contains keys like Classes, Microsoft, and Windows NT, mirroring the registry's layout. Cloud symbols indicate deeper nesting within the structure.](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg8RW1Za0ytuWX-XSA-9nYTvlV8_VHC4wXPs4_OVW3Y7-bRCnVAAG_nQ8Xs354AQ497TsBr-43oft7iVHfvmO9NwTl3TtlnKa6MCrraO0eEiknpK15HdGTiBG1YqysuA1h7qUnranUKJjSGWXSlSJRzxZV3b6SP3sN0-ssJObEb80WCOsZlmEez8LZiUvI/s1200/image8.png "Diagram illustrating the Windows Registry Key Control Block (KCB) tree structure used for key lookups by name or path. The tree starts with the REGISTRY root, branching into top-level keys like MACHINE and USER. It further details the hierarchy under MACHINE, showing SOFTWARE linked to another SOFTWARE node which contains keys like Classes, Microsoft, and Windows NT, mirroring the registry's layout. Cloud symbols indicate deeper nesting within the structure.")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg8RW1Za0ytuWX-XSA-9nYTvlV8_VHC4wXPs4_OVW3Y7-bRCnVAAG_nQ8Xs354AQ497TsBr-43oft7iVHfvmO9NwTl3TtlnKa6MCrraO0eEiknpK15HdGTiBG1YqysuA1h7qUnranUKJjSGWXSlSJRzxZV3b6SP3sN0-ssJObEb80WCOsZlmEez8LZiUvI/s1200/image8.png)

Let's highlight several key points:

* KCB

  Existence:

  There's no guarantee that a corresponding KCB exists for every registry key.



  KCBs are allocated

  lazily

  only when a key is opened, created, or when a KCB that depends on the one being created is about to be allocated.
* Consistent KCB Tree Structure:

  The KCB tree structure is always consistent.



  If a KCB exists for a key, then KCBs for all its ancestors up to the root \Registry key must also exist.
* Cached Information in KCBs:

  KCBs contain cached information from the key node, plus additional runtime information that may not yet be in the hive (e.g., pending transactions).



  Before performing any operation on a key, it's crucial to consult its KCB.
* KCB Uniqueness

  :

  At any given time, there can be only one KCB corresponding to a specific key attached to the tree.



  It's possible for multiple KCBs of the same key to exist in memory, but only if some of them correspond to deleted instances, in which case they are no longer visible in the global tree (only through the handles, until they are closed).



  Before creating a new KCB, the kernel should always ensure that there isn't an existing one, and if there is, use it.



  Failing to maintain this invariant can lead to severe consequences,

  as illustrated by

  [CVE-2023-23420](https://project-zero.issues.chromium.org/issues/42451531)

  .
* KCB Tree and Hives:

  The KCB tree combines key descriptors from different hives and therefore must implement support for "exit nodes" and "entry nodes", as described in the previous blog post.



  Both exit and entry nodes have corresponding KCBs that can be viewed and analyzed in WinDbg.



  Resolving transitions between exit and entry nodes generally involves reading the (

  \_HHIVE\*

  , root cell index) pair from the exit node and then locating and navigating to the corresponding KCB in the destination hive.



  To speed up this process, the kernel uses an optimization that sets the CM\_KCB\_SYM\_LINK\_FOUND flag (0x8) in the exit node's KCB and stores the entry node's KCB address in KCB.LinkTarget, simulating a resolved symbolic link and avoiding the need to look up the entry's KCB every time the key is traversed.



  In the diagram above, entry keys are marked in blue, exit nodes in orange, and the special connection between them by

  the

  connector

  with black squares

  .
* Key Depth:

  Every open key in the system has a depth in the global tree, representing the number of nesting levels separating it from the root.



  This value is stored in the TotalLevels field.



  For example, the root key \Registry has a depth of 1, and the key \Registry\Machine\Software\Microsoft\Windows has a depth of 5.
* Parent KCB Pointer:

  Every initialized KCB structure (whether attached to the tree or not) contains a pointer to its parent KCB in the ParentKcb field.



  The only exception is the global root \Registry, for which this pointer is NULL.

Now that we understand how the KCB tree works conceptually, let's examine how it is represented in memory.



Interestingly, the KCB structure itself doesn't store a list of its subkeys.



Instead, it relies on a simple 32-bit hash of the text string for fast lookups by name.



The hash is calculated by multiplying successive characters of the string by powers of 37, where the first character is multiplied by the highest power and the last by the lowest (37

0

, which is 1)

.



This allows for a straightforward iterative implementation, shown below in C code:

uint32\_t



HashString(

const



std::string&



str)



{

uint32\_t



hash



=



0

;

for



(size\_t



i



=



0

;



i



<



str.size();



i++)



{

hash



=



hash



\*



37



+



toupper(str[i]);

}

return



hash;

}

Some example outputs of the algorithm are:

HashString(

"Microsoft"

)



=



0x7f00cd26

HashString(

"Windows"

)



=



0x2f7de68b

HashString(

"CurrentVersion"

)



=



0x7e25f69d

To calculate the hash of a path with multiple components, the same algorithm steps are repeated.



However, in this case, the hashes of the successive path parts are treated similarly to the letters in the previous example.



Therefore,

the following formula is used

to calculate the hash of the full

"Microsoft\Windows\CurrentVersion"

path:

0x7f00cd26



×



37

2



+



0x2f7de68b



×



37

1



+



0x7e25f69d



×



37

0



=



0x86a158ea

The hash value calculated for each key, based on its path relative to the hive's root, is stored in KCB.ConvKey.Hash.



Consequently, the hash value for the standard system key HKLM\Software\Microsoft\Windows\CurrentVersion is 0x86a158ea.

Every

hive has a directory of the KCBs within it, structured as a hashmap with a fixed number of buckets.



Each bucket comprises a linked list of the KCBs located there.



Internally, this directory is referred to as the "KCB cache" and is represented by the following two fields in the \_CMHIVE structure:

+0x670



KcbCacheTable



:



Ptr64



\_CM\_KEY\_HASH\_TABLE\_ENTRY

+0x678



KcbCacheTableSize



:



Uint4B

KcbCacheTable is a pointer to a dynamically allocated array of \_CM\_KEY\_HASH\_TABLE\_ENTRY structures, and KcbCacheTableSize specifies the number of buckets (i.e., the number of elements in the KcbCacheTable array).



In practice, the size of this KCB cache is

128

buckets for the virtual \Registry hive, 512 for the vast majority of hives loaded in the system, and 1024 for two specific system hives: HKLM\Software and HKLM\System.

Given

a specific key with a name hash denoted as

ConvKey

, its KCB can be found in the cache bucket indexed as follows:

TmpHash



=



101027



\*



(ConvKey



^



(ConvKey



>>



9

));

CacheIndex



=



(TmpHash



^



(TmpHash



>>



9

))



&



(Hive->KcbCacheTableSize



-



1

);

//

// Kcb can be found in Hive->KcbCacheTable[CacheIndex]

//

The operation of translating a key's path hash to its KCB cache table index (excluding the modulo KcbCacheTableSize step) is called "finalization". There's even a WinDbg helper command that can perform this action for us: !reg finalize.



We can test it on the hash we calculated for the "Microsoft\Windows\CurrentVersion" path:

0:



kd>



!reg



finalize



0x86a158ea

Finalized



Hash



for



Hash=0x86a158ea:



0xc2c65312

So, the finalized hash is 0xc2c65312, and since the KCB cache hive size of the SOFTWARE hive is 1024, this means that the index of the HKLM\Software\Microsoft\Windows\CurrentVersion key in the array will be the lowest 10 bits, or 0x312.



We can verify that our calculations are correct by finding the SOFTWARE hive in memory and listing the keys located in its individual buckets

:

0:



kd>



!reg



hivelist

ah

...

|



ffffe10d2dad4000



|



4da2000



|



ffffe10d2da78000



|



3a6000



|



ffffe10d3489f000



|



ffffe10d2d8ff000



|



emRoot\System32\Config\SOFTWARE

...

0:



kd>



!reg



openkeys



ffffe10d2dad4000

...

Index



312:



86a158ea



kcb=ffffe10d2d576a30



cell=000a58e8



f=00200000



\REGISTRY\MACHINE\SOFTWARE\MICROSOFT\WINDOWS\CURRENTVERSION

...

As we can see, o

ur calculations have been proven to be accurate.



We could achieve a similar result with the !reg hashindex command

, which

takes the address of the \_HHIVE



object and the ConvKey for a given key, and then prints out information about the corresponding bucket.

Within a single bucket in the KCB cache, all the KCBs are linked together in a singly-linked list

starting

at the \_CM\_KEY\_HASH\_TABLE\_ENTRY.Entry pointer.



The

subsequent



elements are accessible through the \_CM\_KEY\_HASH.NextHash field, which points to the KCB.KeyHash structure in the next KCB on the list.



A diagram of this data structure is shown below:

[![Diagram of the Windows Registry KCB cache structure. A pointer from the _CMHIVE structure references a _CM_KEY_HASH_TABLE_ENTRY array (hash table). Each entry/bucket in this array points to a singly-linked list of Key Control Blocks (KCBs). Within each KCB, the NextHash field points to the KeyHash structure of the subsequent KCB in the list, forming the chain.](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhs1mVeihbkGh07sygFQgByTbDezW9Mn2DKrqFOvnfA8ZcmJb7VDjevJ3pFF4fQ8gTi4BsmPwkZmoISPzFhe5Usgdgr-wj2BvFuAkXe5PYuzSK1TlHa1UTDqAoFV8A288SVDqrfxWddB90RKKOeCFiW6_I2fqvqGK4OGlITg5rsU5dHPfvCX1TiEhyphenhyphenoi_U/s1200/image6.png "Diagram of the Windows Registry KCB cache structure. A pointer from the _CMHIVE structure references a _CM_KEY_HASH_TABLE_ENTRY array (hash table). Each entry/bucket in this array points to a singly-linked list of Key Control Blocks (KCBs). Within each KCB, the NextHash field points to the KeyHash structure of the subsequent KCB in the list, forming the chain.")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhs1mVeihbkGh07sygFQgByTbDezW9Mn2DKrqFOvnfA8ZcmJb7VDjevJ3pFF4fQ8gTi4BsmPwkZmoISPzFhe5Usgdgr-wj2BvFuAkXe5PYuzSK1TlHa1UTDqAoFV8A288SVDqrfxWddB90RKKOeCFiW6_I2fqvqGK4OGlITg5rsU5dHPfvCX1TiEhyphenhyphenoi_U/s1200/image6.png)

Now that

we understand how the KCB objects are internally organized, let's examine how name lookups are implemented.



Suppose we want to take a single step through a path and find the KCB of the next subkey based on its parent KCB and the key name.

The

process is as follows (assuming the parent is not an exit node):

1. Get the pointer to the hive descriptor on which we are currently operating from ParentKcb->KeyHive.
2. Calculate the hash of the subkey name based on its full path relative to the hive in which it is located.
3. Calculate the appropriate index in the KCB cache based on the name hash and iterate through the linked list, comparing:

1. The hash of the key name.
2. The pointer to the parent KCB.
3. If both of the above match, perform a full comparison of the key name.



   If it matches, we have found the subkey.

The

process is particularly interesting because it is not based on directly iterating through the subkeys of a given key, but instead on iterating through all the keys in the particular cache bucket.

T

hanks to the use of hashing, the vast majority of checks of potential candidates for the sought-after subkey are reduced to a single comparison of two 32-bit numbers, making the whole process quite efficient. The performance is mostly dependent on the total number of keys in the hive and the number of hash collisions for the specific cache index.

If you'd like to dive deeper into the implementation of KCB tree traversal, I recommend analyzing the internal function CmpFindKcbInHashEntryByName, which performs a single step through the tree as described above. Another useful function to analyze is CmpPerformCompleteKcbCacheLookup, which recursively searches the tree to find the deepest KCB object corresponding to one of the elements of a given path.

For those experimenting in WinDbg, here are a few useful commands related to KCBs and their trees:

* !reg findkcb:

  This command finds the address of the KCB in the global tree that corresponds to the given fully qualified registry path, if it exists.
* !reg querykey:

  Similar to the command above, but in addition to providing the KCB address, it also prints the hive descriptor address, the corresponding key node address, and information about subkeys and values of the given key.
* !reg kcb:

  This command prints basic information about a key based on its KCB. Its advantage is that it translates flag names into their textual equivalents (e.g., CompressedName, NoDelete, HiveEntry, etc.), but it often doesn't provide the specific information one is looking for. In that case, it might be necessary to use the dt \_CM\_KEY\_CONTROL\_BLOCK command to dump the entire structure.

## Other structures

So far, t

his blog post has described only a few of the most important registry structures,

which are

essential to know for anyone conducting research in this area.



However, in total, there are over 150 different structures used in the Windows kernel and related to the registry

, and o

nly about half are documented through debug symbols or on Microsoft's website.



While it's impossible to detail the operation and function of all of these structures in one article, this section aims to at least provide an overview of a majority of them, to note which of them are publicly available, and to briefly describe how they are used internally.

The layout of many structures corresponding to the most complex mechanisms is publicly unknown

at the time of writing

and requires significant time and energy to reconstruct.



Even then, the correct meaning of each field and flag cannot be guaranteed.



Therefore, the information below should be used with caution and verified against the specific Windows version(s) in question

before relying on it in any way.

### Key opening/creation

|  |  |  |
| --- | --- | --- |
| In PDB | Structure name | Description |
| ❌ | Parse context | Given that the registry is integrated with the standard Windows object model, all operations on registry paths (both absolute and relative) must be performed through the standard NT Object Manager interface.  For example, the NtCreateKey syscall calls the CmCreateKey helper function.    At this point, there are no further calls to Configuration Manager, but instead, there is a call to ObOpenObjectByNameEx (a more advanced version of  [ObOpenObjectByName](https://learn.microsoft.com/en-us/windows/win32/devnotes/obopenobjectbyname-function)  ).    Several levels down, the kernel will transfer execution back to the registry code, specifically to the CmpParseKey callback, which is the entry point responsible for handling all path operations (i.e., all key open/create actions).    This means that the CmCreateKey and CmpParseKey functions, which work together, cannot pass an arbitrary number of input and output arguments to each other.  T  hey only have one pointer (ParseContext) at their disposal, which can serve as a communication channel.    Thus, the agreement between these functions is that the pointer points to a special "parse context" structure, which has three main roles  :   * Pass the input configuration of a given operation, e.g. information about:  * operation mode (open/create), * transactionality of the operation, * following of    symbolic links, * flags related to WOW64 functionality    , * optional    class    data of the created key    .  * Pass some return information, such as whether the key was opened or created, * Cache certain information within a single "parse" request, e.g.:  * information on whether registry virtualization is enabled for a given process, * when following a symbolic link, a pointer to the originating hive descriptor, in order to check whether the given transition is allowed within the hive trust class, * when following a symbolic link, a pointer to the KCB of its target (or the closest possible ancestor).   Reconstructing the layout of this structure is a critical step in getting a better understanding of how the key opening/creation process works internally. |
| ❌ | Path info | When a client references a key by name, one of the first actions taken by the CmpParseKey function (or more specifically, CmpDoParseKey) is to take the string representing that name (absolute or relative), break it into individual parts separated by backslashes, and calculate the 32-bit hashes for each of them.    This ensures that parsing only occurs once and doesn't need to be repeated.    The structure where the result of this operation is stored is called "path info"  .    According to the  [documentation](https://learn.microsoft.com/en-us/windows/win32/sysinfo/registry-element-size-limits)  , a single registry path reference can contain a maximum of 32 levels of nesting.    Therefore, the path info structure allows for the storage of 32 elements, in the following way: the first 8 elements being present directly within the structure, and if the path is deeply nested, an additional 24 elements within a supplementary structure allocated on-demand from kernel pools.    The functions that operate on this object are CmpComputeComponentHashes, CmpExpandPathInfo, CmpValidateComponents, CmpGetComponentNameAtIndex, CmpGetComponentHashAtIndex, and CmpCleanupPathInfo.    Interestingly, I discovered an off-by-one bug in the CmpComputeComponentHashes function, which allows an attacker to write 25 values into a 24-element array.    However, due to a fortunate coincidence, path info structures are allocated from a special lookaside list with allocation sizes significantly larger than the length of the structure itself.    As a result, this buffer overflow is not exploitable in practice, which has also been confirmed by Microsoft.    More information about this issue, as well as the reversed definition of this structure, can be found in  my    [original report](https://github.com/googleprojectzero/p0tools/tree/master/WinRegLowSeverityBugs/Reports/03_CmpComputeComponentHashes_nested_path_overflow)  . |

### Key notifications

|  |  |  |
| --- | --- | --- |
| In PDB | Structure name | Description |
| ✅ | \_CM\_NOTIFY\_BLOCK | The first time  [RegNotifyChangeKeyValue](https://learn.microsoft.com/en-us/windows/win32/api/winreg/nf-winreg-regnotifychangekeyvalue)  or the underlying  [NtNotifyChangeMultipleKeys](https://learn.microsoft.com/en-us/windows/win32/api/winternl/nf-winternl-ntnotifychangemultiplekeys)  syscall is called on a given handle, a notify block structure is assigned to the corresponding key body object. This structure serves as the central control point for all notification requests made on that handle in the future. It also stores the configuration defined in the initial API call, which, once set, cannot be changed without closing and reopening the key. This is in line with the official MSDN documentation:    "This function should not be called multiple times with the same value for the hKey but different values for the bWatchSubtree and dwNotifyFilter parameters. The function will succeed but the changes will be ignored. To change the watch parameters, you must first close the key handle by calling RegCloseKey, reopen the key handle by calling RegOpenKeyEx, and then call RegNotifyChangeKeyValue with the new parameters."    The !reg notifylist command in WinDbg can list all active notify blocks in the system, allowing you to check which keys are currently being monitored for changes. |
| ❌ | Post block | Each post block object corresponds to a single wait for changes to a given key. Many post block objects can be assigned to one notify block object at the same time. The network of relationships in this structure becomes even more complex when using the NtNotifyChangeMultipleKeys syscall with a non-empty SubordinateObjects argument, in which case two separate post blocks share a third data structure (the so-called post block union). However, the details of this topic are beyond the scope of this post.    The WinDbg !reg postblocklist command allows you to see how many active post blocks are assigned to each process/thread, but unfortunately, it does not show any detailed information about their contents. |

### Registry callbacks

|  |  |  |
| --- | --- | --- |
| In PDB | Structure name | Description |
| ✅ | REG\_\*\_INFORMATION | These structures are used for supplying callbacks with precise information about operations performed on the registry, and are part of the documented Windows interface.    Consequently, not only their definitions but also detailed descriptions of the meaning of each field are published directly by Microsoft.    A complete list of these structures can be found on MSDN, e.g., on the  [EX\_CALLBACK\_FUNCTION callback function (wdm.h)](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdm/nc-wdm-ex_callback_function)  page.    However, I have found in my research that in addition to the official registry callback interface, there is also a less official extension  that Microsoft uses internally in VRegDriver, the module that supports differencing hives  .    If a given client, instead of using the official  [CmRegisterCallbackEx](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdm/nf-wdm-cmregistercallbackex)  function, calls the internal CmpRegisterCallbackInternal function with the fifth argument set to 1, this callback will be internally marked as "extended".    Extended callbacks, in addition to the information provided by the standard structures, also receive a handful of additional information related to differencing hives and layered keys.    At the time of writing, the differences occur in the structures representing the RegNtPreLoadKey, RegNtPreCreateKeyEx, RegNtPreOpenKeyEx actions and their "post" counterparts. |
| ❌ | Callback descriptor | The structure represents a single registry callback registered through the  [CmRegisterCallback](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdm/nf-wdm-cmregistercallback)  or  [CmRegisterCallbackEx](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdm/nf-wdm-cmregistercallbackex)  API. Once allocated, it is attached to a double-linked list represented by the global  CallbackListHead  object. |
| ❌ | Object context descriptor | A  descriptor structure for a key body-specific context that can be assigned through the  [CmSetCallbackObjectContext](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdm/nf-wdm-cmsetcallbackobjectcontext)  API. This descriptor is then inserted into a linked list that starts at \_CM\_KEY\_BODY.ContextListHead. |
| ❌ | Callback context | A  n internal structure used in the CmpCallCallBacksEx function to store the current state during the callback invocation process.    For example, it's used to invoke the appropriate "post" type callbacks in case of an error in one of the "pre" type callbacks.    These objects are freed by the dedicated CmpFreeCallbackContext function, which additionally caches a certain number of allocations in the global CmpCallbackContextSList list.    This allows future requests for objects of this type to be quickly fulfilled. |

### Registry virtualization

|  |  |  |
| --- | --- | --- |
| In PDB | Structure name | Description |
| ❌ | Replication stack | A  core task of registry virtualization is the replication of keys, which involves creating an identical copy of a given key structure.    This occurs under the path HKU\<SID>\_Classes\VirtualStore when an application, subject to virtualization, attempts to create a key in a location where it lacks proper permissions.    The entire operation is coordinated by the CmpReplicateKeyToVirtual function and consists of two main stages.    First, a "replication stack" object is created and initialized in the CmpBuildVirtualReplicationStack function.    This object specifies the precise key structure to be created within the virtualization process.    Second, the actual creation of these keys based on this object occurs within the CmpDoBuildVirtualStack function. |

### Transactions

|  |  |  |
| --- | --- | --- |
| In PDB | Structure name | Description |
| ✅ | \_KTRANSACTION | A  structure corresponding to a KTM transaction object, which is created by the  [CreateTransaction](https://learn.microsoft.com/en-us/windows/win32/api/ktmw32/nf-ktmw32-createtransaction)  function or its low-level equivalent  [NtCreateTransaction](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdm/nf-wdm-ntcreatetransaction)  . |
| ❌ | Lightweight transaction object | A  direct counterpart of \_KTRANSACTION, but for lightweight transactions, created by the NtCreateRegistryTransaction system call.  It is very simple and only  consists of a bitmask of the current transaction state, a push lock for synchronization, and a pointer to the corresponding \_CM\_TRANS object. |
| ✅ | \_CM\_KCB\_UOW | The  structure represents a single, active transactional operation linked to a specific key.    In some scenarios, one logical operation corresponds to one such object (e.g., the UoWSetSecurityDescriptor type).    In other cases, multiple UoWs are created for a single operation (e.g., UoWAddThisKey assigned to a newly created key, and UoWAddChildKey assigned to its parent).    This critical structure has multiple functions.    The key ones are connecting to KCB intent locks and keeping any pending state related to a given operation, both before and during the transaction commit phase. |
| ✅ | \_CM\_UOW\_\* | A  uxiliary sub-structures of \_CM\_KCB\_UOW, which store information about the temporary state of the registry associated with a specific type of transactional operation.  Specifically, the four structures are  :  \_CM\_UOW\_KEY\_STATE\_MODIFICATION  , \_CM\_UOW\_SET\_SD\_DATA, \_CM\_UOW\_SET\_VALUE\_KEY\_DATA and \_CM\_UOW\_SET\_VALUE\_LIST\_DATA. |
| ✅ | \_CM\_TRANS | A  descriptor of a specific registry transaction, usually associated with a particular hive.    In special cases, if operations are performed on multiple hives within a single transaction, then multiple  \_CM\_TRANS objects may exist for it.    Given the address of the \_CM\_TRANS object, it is possible to list all operations associated with this transaction in WinDbg using the !reg uowlist command. |
| ✅ | \_CM\_RM | A  descriptor of a specific  resource manager  .    It only exists if the given hive has KTM transactions enabled  , and  never exists for app hives or hives loaded with the REG\_HIVE\_NO\_RM flag.    Think of this structure as being associated with one set of .blf / .regtrans-ms log files, which usually means one \_CM\_RM structure is assigned to one hive.    The exception is system hives (e.g. SOFTWARE, SYSTEM etc.) which all share the same resource manager that exists under the CmRmSystem global variable.    Given the address of a \_CM\_RM object in WinDbg, you can list all associated transactions using the !reg translist command. |
| ✅ | \_CM\_INTENT\_LOCK | This structure represents an intent lock, with two instances (KCBLock and KeyLock) residing in the KCB. Their primary function is to ensure key consistency by preventing the assignment of two different transactions that contain conflicting modifications of a key.    Given the object's address, WinDbg's !reg ixlock command  can  display some details about it. |
| ❌ | Serialized log records | KTM transacted registry operations are logged to .blf files on disk to enable consistent state restoration in case of unexpected shutdown during transaction commit.    The CmAddLogForAction function serializes the \_CM\_KCB\_UOW object into a flat buffer and writes it to the log file using the CLFS interface.    While the \_CM\_KCB\_UOW structure can be found in public symbols, their corresponding serialized representations cannot.    Notably, there was an information disclosure vulnerability (  [CVE-2023-28271](https://project-zero.issues.chromium.org/issues/42451559)  ) that was directly related to these structures. |
| ❌ | Rollback packet | When a client performs a non-transactional operation that modifies a key, and there's an active transaction associated with that key, the transaction must be rolled back before the operation can be executed to prevent an inconsistent state.    This is achieved using a structure that contains a list of transactions to be rolled back.    This structure is passed to the CmpAbortRollbackPacket function, which carries out the rollback.    Although the official layout of this structure is unknown, in practice it is quite simple, consisting of three fields: the current capacity, the current fill level of the list, and a pointer to a dynamically allocated array of transactions. |

### Differencing hives (VRegDriver)

|  |  |  |
| --- | --- | --- |
| In PDB | Structure name | Description |
| ❌ | IOCTL input structures | The VRegDriver module works by creating the \Device\VRegDriver device, and communicates with its clients by supporting nine distinct IOCTLs within the corresponding VrpIoctlDeviceDispatch handler function.    These IOCTLs, exclusively accessible to administrator users, facilitate loading and unloading differencing hives, configuring registry redirections for specific containers, and a few other operations.    Each IOCTL requires a specific input data structure, none of which are officially documented.    Therefore, practical use of this interface necessitates reverse engineering the required structures to understand their initialization.    An example of a reversed structure, corresponding to IOCTL 0x220008 and  provisionally    named VRP\_LOAD\_DIFFERENCING\_HIVE\_INPUT, was showcased in  [blog post #4](https://googleprojectzero.blogspot.com/2024/10/the-windows-registry-adventure-4-hives.html)  .    This enabled the creation of a proof-of-concept exploit for a differencing hive vulnerability (  [CVE-2023-36404](https://project-zero.issues.chromium.org/issues/42451625)  ), demonstrating the ability to load custom hives and, consequently, expose the flaw. |
| ❌ | Silo context | This silo-specific context structure is set by the VRegDriver during silo initialization using the  [PsInsertPermanentSiloContext](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntddk/nf-ntddk-psinsertpermanentsilocontext)  function.    It is later retrieved by  [PsGetPermanentSiloContext](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntddk/nf-ntddk-psgetpermanentsilocontext)  and used during both IOCTL handling and path translation for containerized processes.    A brief analysis suggests that it primarily contains the GUID of the associated silo, a push lock used for synchronization, and a user-configured list of namespaces for the given container, which is a set of source and target paths between which redirection should occur. |
| ❌ | Key context | This structure stores the context specific to a particular key being subject to path translation within a silo.    It is usually allocated for each key opened within the context of a containerized process, and assigned to its key body using the  [CmSetCallbackObjectContext](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdm/nf-wdm-cmsetcallbackobjectcontext)  API. It primarily stores the original path of the key before translation    —    as the client believes it has access to    —    and several other auxiliary fields. |
| ❌ | Callback context (open/create) | The callback-specific context structure stores shared data between "pre" and "post" callbacks for a given operation.    This context is generally accessed through the CallContext field within the REG\_  \*  \_INFORMATION structure relevant to the specific operation.    In practice, VRegDriver only has one instance of a special structure defined for this purpose, used when handling the RegNtPreCreateKeyEx/RegNtPreOpenKeyEx callbacks.    It saves specific data (RootObject, CompleteName, RemainingName) before the open/create request, to restore their original values in the "post" callback. |
| ❌ | Extra parameter | This structure also appears to be used for temporarily storing the original key path during translation.  However, i  ts scope encompasses the entire key creation/opening process, rather than just a single callback.    This means it can store information across callbacks, even when symbolic links or write-through hives are encountered during path traversal, causing the CmpParseKey function to return STATUS\_REPARSE or STATUS\_REPARSE\_GLOBAL and restart the path lookup process.    Although the concept of a  whole operation context  seems broadly applicable, currently there is only one type of "extra parameter"  being used  , represented by the GUID VRP\_ORIGINAL\_KEY\_NAME\_PARAMETER\_GUID {85b8669a-cfbb-4ac0-b689-6daabfe57722}. |

### Layered keys

|  |  |  |
| --- | --- | --- |
| In PDB | Structure name | Description |
| ✅ | \_CM\_KCB\_LAYER\_INFO | This is likely the only structure related to layered keys whose definition is public.    It is part of every KCB and contains information about the placement of the key in the global,  "  vertical" tree of layered key instances.    In practice, this means that it stores a pointer to the KCB at one level lower (its parent, so to speak), and the head of a linked list with KCBs at one level higher (KCB.LayerHeight+1  ), if any exist. |
| ❌ | Key node stack | A stack containing all instances of a given layered key, starting from its level all the way down to level zero (the base key).    Each key in this structure is represented by a (Hive, KeyCell) pair.    If the key actually exists at a given level (KeyCell ≠ -1, indicating a state other than Merge-Unbacked), it is also represented by a direct, resolved pointer to its \_CM\_KEY\_NODE structure.    Since Windows 10 introduced support for layered keys, many places in the code that previously identified a single key as \_CM\_KEY\_NODE  \*  now require passing the entire key node stack structure.    This is because operations on layered keys usually require knowledge of the state of lower level keys (e.g. their layered semantics, subkeys, values), not just the key represented by the handle used by the caller.    Places where the key node stack structure is used can be identified by calls to its related helper functions, such as those for initialization (CmpInitializeKeyNodeStack) and cleanup (CmpCleanupKeyNodeStack), as well as any others containing the string "KeyNodeStack". |
| ❌ | KCB stack | This structure, analogous to the key node stack, represents keys using KCBs.    Its use is most clearly revealed by references to the CmpStartKcbStack and CmpStartKcbStackForTopLayerKcb functions in code, though many other internal routines with "KcbStack" in their names also operate on it.    Both the KCB stack and the key node stack share an optimization where the first two levels are stored inline, with additional levels allocated in kernel pools only when necessary.    This is likely due to the fact that most systems, even those with layered keys, typically only use one level of nesting (two levels total).  Thus, this  optimization avoids costly memory allocation and deallocation in these common scenarios. |
| ❌ | Enum stack | This data structure allows for the enumeration of subkeys within a given layered key.    Its primary use is within the CmpEnumerateLayeredKey function, which serves as the handler for the  [NtEnumerateKey](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdm/nf-wdm-zwenumeratekey)  operation specifically for layered keys.    At an even higher level, this corresponds to the  [RegEnumKeyExW](https://learn.microsoft.com/en-us/windows/win32/api/winreg/nf-winreg-regenumkeyexw)  API function.    The complexity of this structure is evident by the fact that there are 19 internal helper functions, all starting with the name CmpKeyEnumStack, that operate on it. |
| ❌ | Enum resume context | This data structure, directly tied to the subkey enumeration, primarily serves as an optimization mechanism.    After executing a specific number (N) of enumeration steps, it stores the internal state of the enum stack.    This allows subsequent requests for subkey N+1 to resume the enumeration process from the previous point, bypassing the need to repeat the initial steps.    Linked to a specific handle, it is stored within \_CM\_KEY\_BODY.EnumerationResumeContext.    The KCB.SequenceNumber field, directly related to this structure, monitors whether a given key has significantly changed since a previous point in time.    This enables the CmpKeyEnumStackVerifyResumeContext helper function to determine if the current registry state is consistent enough for the existing enumeration resume context to be used for further enumeration, or if the entire process needs to be restarted. |
| ❌ | Value enum stack | This data structure, used to enumerate values for layered keys, is similarly complex as those used to list subkeys.    The main function utilizing it is CmEnumerateValueFromLayeredKey.    Additionally, there are 10 helper functions named CmpValueEnumStack[...] that operate on this structure. |
| ❌ | Sorted value enum stack | The structure is similar to the standard value enum stack, but is used to iterate over the values of a given layered key while preserving lexicographical order.  H  elper functions from the CmpSortedValueEnumStack[...] family (9 in total) correspond to this structure.    This functionality is used exclusively in the CmpGetValueCountForKeyNodeStack function, which is responsible for returning the number of values for a given key.    The reason for the existence of this mechanism in parallel with the regular "value enum stack" is not entirely clea  r, but  I suspect it serves as an optimization for value counting operations.    This is supported by the fact that while layered keys first appeared in Windows 10 1607 (Redstone, build 14393), the sorted value enum stack was not introduced until the later version of Windows 10 1703 (Redstone 2, build 15063).  In the first iteration of the layered key implementation  , CmpGetValueCountForKeyNodeStack was implemented using the standard value enum stack.    This lends credibility to the hypothesis that these mechanisms are functionally equivalent, but the "sorted" version is faster at counting unique values when direct access to them is not required. |
| ❌ | Subtree enumerator | This structure enables the enumeration of both the direct subkeys of a layered key and all its deeper descendants.    It is relatively complex, and its associated functions begin with CmpSubtreeEnumerator[...] (also 9 in total).    This mechanism is primarily needed to implement the "rename" operation on layered keys.    First, it allows verification that the caller has KEY\_READ and DELETE permissions for all descendant keys in the subtree  , and s  econd, it enables setting the LayerSemantics value for these descendants to Supersede-Tree (0x3). |
| ❌ | Discard/replace context | This data structure is employed during key deletion to ensure that KCB structures corresponding to higher-level Merge-Unbacked keys reliant on the deleted key are also marked as deleted.    Subsequently, "fresh" KCB objects representing the non-existent key are inserted into the tree in their place.    The two primary functions associated with this mechanism are CmpPrepareDiscardAndReplaceKcbAndUnbackedHigherLayers and CmpCommitDiscardAndReplaceKcbAndUnbackedHigherLayers. |

## Conclusion

The goal of this post was to provide a thorough overview of the structures used in the Configuration Manager subsystem in Windows, with particular emphasis on the most important and frequently used ones, i.e. those describing hives and keys.



I wanted to share this knowledge because there are not many publicly available sources that accurately describe the registry's operation from the implementation side, especially relevant to the most recent code developments in Windows 10 and 11.



I would also like to once again use this opportunity to appeal to Microsoft to make more information available through public PDB symbols – this would greatly facilitate the work of security researchers in the future.

This post concludes the part of the series focusing solely on the inner workings of the registry.



In the next, seventh installment,

we will shift our perspective and examine the registry's role in the overall security of the system, with a deep focus on vulnerability research.

Stay tuned!
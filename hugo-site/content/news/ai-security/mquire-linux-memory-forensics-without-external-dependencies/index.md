---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-02-26T06:15:15.898287+00:00'
exported_at: '2026-02-26T06:15:18.520878+00:00'
feed: https://blog.trailofbits.com/feed/
language: en
source_url: https://blog.trailofbits.com/2026/02/25/mquire-linux-memory-forensics-without-external-dependencies
structured_data:
  about: []
  author: ''
  description: "\n                We’re open-sourcing mquire, a tool that analyzes
    Linux memory dumps without requiring any external debug information.\n            "
  headline: 'mquire: Linux memory forensics without external dependencies'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://blog.trailofbits.com/2026/02/25/mquire-linux-memory-forensics-without-external-dependencies
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: 'mquire: Linux memory forensics without external dependencies'
updated_at: '2026-02-26T06:15:15.898287+00:00'
url_hash: 318c1c37c3df3674cb14faeb4cf400f24fb497e6
---

If you’ve ever done Linux memory forensics, you know the frustration: without debug symbols that match the exact kernel version, you’re stuck. These symbols aren’t typically installed on production systems and must be sourced from external repositories, which quickly become outdated when systems receive updates. If you’ve ever tried to analyze a memory dump only to discover that no one has published symbols for that specific kernel build, you know the frustration.

Today, we’re open-sourcing
[mquire](https://github.com/trailofbits/mquire)
, a tool that eliminates this dependency entirely. mquire analyzes Linux memory dumps without requiring any external debug information. It works by extracting everything it needs directly from the memory dump itself. This means you can analyze unknown kernels, custom builds, or any Linux distribution, without preparation and without hunting for symbol files.

For forensic analysts and incident responders, this is a significant shift: mquire delivers reliable memory analysis even when traditional tools can’t.

## The problem with traditional memory forensics

Memory forensics tools like
[Volatility](https://github.com/volatilityfoundation/volatility3)
are essential for security researchers and incident responders. However, these tools require debug symbols (or “profiles”) specific to the exact kernel version in the memory dump. Without matching symbols, analysis options are limited or impossible.

In practice, this creates real obstacles. You need to either source symbols from third-party repositories that may not have your specific kernel version, generate symbols yourself (which requires access to the original system, often unavailable during incident response), or hope that someone has already created a profile for that distribution and kernel combination.

mquire takes a different approach: it extracts both type information and symbol addresses directly from the memory dump, making analysis possible without any external dependencies.

## How mquire works

mquire combines two sources of information that modern Linux kernels embed within themselves:

**Type information from BTF**
:
[BPF Type Format](https://www.kernel.org/doc/html/next/bpf/btf.html)
is a compact format for type and debug information originally designed for eBPF’s “compile once, run everywhere” architecture. BTF provides structural information about the kernel, including type definitions for kernel structures, field offsets and sizes, and type relationships. We’ve repurposed this for memory forensics.

**Symbol addresses from Kallsyms**
: This is the same data that populates
`/proc/kallsyms`
on a running system—the memory locations of kernel symbols. By scanning the memory dump for Kallsyms data, mquire can locate the exact addresses of kernel structures without external symbol files.

By combining type information with symbol locations, mquire can find and parse complex kernel data structures like process lists, memory mappings, open file handles, and cached file data.

### Kernel requirements

* **BTF support**
  : Kernel 4.18 or newer with BTF enabled (most modern distributions enable it by default)
* **Kallsyms support**
  : Kernel 6.4 or newer (due to format changes in
  `scripts/kallsyms.c`
  )

These features have been consistently enabled on major distributions since they’re requirements for modern BPF tooling.

## Built for exploration

After initialization, mquire provides an interactive SQL interface, an approach directly inspired by
[osquery](https://github.com/osquery/osquery)
. This is something I’ve wanted to build ever since my first Querycon, where I discussed forensics capabilities with other osquery maintainers. The idea of bringing osquery’s intuitive, SQL-based exploration model to memory forensics has been on my mind for years, and mquire is the realization of that vision.

You can run one-off queries from the command line or explore interactively:

```
$ mquire query --format json snapshot.lime 'SELECT comm, command_line FROM
tasks WHERE command_line NOT NULL and comm LIKE "%systemd%" LIMIT 2;'
{
  "column_order": [
    "comm",
    "command_line"
  ],
  "row_list": [
    {
      "comm": {
        "String": "systemd"
      },
      "command_line": {
        "String": "/sbin/init splash"
      }
    },
    {
      "comm": {
        "String": "systemd-oomd"
      },
      "command_line": {
        "String": "/usr/lib/systemd/systemd-oomd"
      }
    }
  ]
}
```

Figure 1: mquire listing tasks containing systemd

The SQL interface enables relational queries across different data sources. For example, you can join process information with open file handles in a single query:

```
mquire query --format json snapshot.lime 'SELECT tasks.pid,
task_open_files.path FROM task_open_files JOIN tasks ON tasks.tgid =
task_open_files.tgid WHERE task_open_files.path LIKE "%.sqlite" LIMIT 2;'
{
  "column_order": [
    "pid",
    "path"
  ],
  "row_list": [
    {
      "path": {
        "String": "/home/alessandro/snap/firefox/common/.mozilla/firefox/
        4f1wza57.default/cookies.sqlite"
      },
      "pid": {
        "SignedInteger": 2481
      }
    },
    {
      "path": {
        "String": "/home/alessandro/snap/firefox/common/.mozilla/firefox/
        4f1wza57.default/cookies.sqlite"
      },
      "pid": {
        "SignedInteger": 2846
      }
    }
  ]
}
```

Figure 2: Finding processes with open SQLite databases

This relational approach lets you reconstruct complete file paths from kernel
`dentry`
objects and connect them with their originating processes—context that would require multiple commands with traditional tools.

## Current capabilities

mquire currently provides the following tables:

* `os_version`
  and
  `system_info`
  : Basic system identification
* `tasks`
  : Running processes with PIDs, command lines, and binary paths
* `task_open_files`
  : Open files organized by process
* `memory_mappings`
  : Memory regions mapped by each process
* `boot_time`
  : System boot timestamp
* `dmesg`
  : Kernel ring buffer messages
* `kallsyms`
  : Kernel symbol addresses
* `kernel_modules`
  : Loaded kernel modules
* `network_connections`
  : Active network connections
* `network_interfaces`
  : Network interface information
* `syslog_file`
  : System logs read directly from the kernel’s file cache (works even if log files have been deleted, as long as they’re still cached in memory)
* `log_messages`
  : Internal mquire log messages

mquire also includes a
`.dump`
command that extracts files from the kernel’s file cache. This can recover files directly from memory, which is useful when files have been deleted from disk but remain in the cache. You can run it from the interactive shell or via the command line:

```
mquire command snapshot.lime '.dump /output/directory'
```

For developers building custom analysis tools, the
`mquire`
library crate provides a reusable API for kernel memory analysis.

## Use cases

mquire is designed for:

* **Incident response**
  : Analyze memory dumps from compromised systems without needing to source matching debug symbols.
* **Forensic analysis**
  : Examine what was running and what files were accessed, even on unknown or custom kernels.
* **Malware analysis**
  : Study process behavior and file operations from memory snapshots.
* **Security research**
  : Explore kernel internals without specialized setup.

## Limitations and future work

mquire can only access kernel-level information; BTF doesn’t provide information about user space data structures. Additionally, the Kallsyms scanner depends on the data format from the kernel’s
`scripts/kallsyms.c`
; if future kernel versions change this format, the scanner heuristics may need updates.

We’re considering several enhancements, including expanded table support to provide deeper system insight, improved caching for better performance, and DMA-based external memory acquisition for real-time analysis of physical systems.

## Get started

mquire is available on
[GitHub](https://github.com/trailofbits/mquire)
with prebuilt binaries for Linux.

To acquire a memory dump, you can use
[LiME](https://github.com/504ensicsLabs/LiME)
:

```
insmod ./lime-x.x.x-xx-generic.ko 'path=/path/to/dump.raw format=padded'
```

Then you can run mquire:

```
# Interactive session
$ mquire shell /path/to/dump.raw

# Single query
$ mquire query /path/to/dump.raw 'SELECT * FROM os_version;'

# Discover available tables
$ mquire query /path/to/dump.raw '.schema'
```

We welcome contributions and feedback. Try
[mquire](https://github.com/trailofbits/mquire)
and let us know what you think.
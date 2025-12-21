---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2025-12-21T12:03:12.707074+00:00'
exported_at: '2025-12-21T12:03:15.311721+00:00'
feed: https://isc.sans.edu/rssfeed.xml
language: en
source_url: https://isc.sans.edu/diary/rss/32580
structured_data:
  about: []
  author: ''
  description: 'DLLs & TLS Callbacks, Author: Didier Stevens'
  headline: DLLs &#x26; TLS Callbacks, (Fri, Dec 19th)
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://isc.sans.edu/diary/rss/32580
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: DLLs &#x26; TLS Callbacks, (Fri, Dec 19th)
updated_at: '2025-12-21T12:03:12.707074+00:00'
url_hash: eb95a27df31d6c2303f98eea86896c29ed3e2c63
---

Xavier's diary entry "
[Abusing DLLs EntryPoint for the Fun](https://isc.sans.edu/diary/Abusing+DLLs+EntryPoint+for+the+Fun/32562/)
" inspired me to do some tests with TLS Callbacks and DLLs.

TLS stands for Thread Local Storage. TLS Callbacks are an execution mechanism in Windows PE files that lets code run automatically when a process or thread starts, before the program’s normal entry point is reached. I've done tests in the past with EXEs and TLS Callbacks, but never with DLLs.

In Windows, TLS is used to give each thread its own copy of certain variables. To support this, the PE format has a TLS directory (IMAGE\_TLS\_DIRECTORY) that describes:

* Where TLS data is stored
* How large it is
* A list of callback functions

My
[pecheck.py](https://github.com/DidierStevens/DidierStevensSuite/blob/master/pecheck.py)
tool lists TLS callbacks:

![](https://isc.sans.edu/diaryimages/images/20251217-193116.png)

I used the following code for a DLL with a TLS callback:

```
#include <windows.h>

// Declare TLS callback section
#pragma section(".CRT$XLB", read)

// TLS callback function
void NTAPI MyTlsCallback(PVOID hModule, DWORD dwReason, PVOID pReserved)
{
    if (dwReason == DLL_PROCESS_ATTACH)
    {
        MessageBoxA(NULL, "TLS Callback fired", "TLS", MB_OK);
    }
}

// Force linker to include TLS directory symbol
#ifdef _WIN64
#pragma comment(linker, "/INCLUDE:_tls_used")
#pragma comment(linker, "/INCLUDE:tls_callback_func")
#else
#pragma comment(linker, "/INCLUDE:__tls_used")
#pragma comment(linker, "/INCLUDE:_tls_callback_func")
#endif

// Place pointer in TLS callback section (extern "C" prevents mangling)
extern "C" __declspec(allocate(".CRT$XLB"))
PIMAGE_TLS_CALLBACK tls_callback_func = MyTlsCallback;

// Standard DllMain
BOOL APIENTRY DllMain(HMODULE hModule, DWORD ul_reason_for_call, LPVOID lpReserved)
{
    if (ul_reason_for_call == DLL_PROCESS_ATTACH)
        MessageBoxA(NULL, "DllMain fired", "DllMain", MB_OK);
    return TRUE;
}
```

And compiled it with Visual Studio C++:

```
cl /nologo /EHsc /LD tls_dll.cpp user32.lib
```

I used rundll32 to load the DLL.

The callback function got executed:

![](https://isc.sans.edu/diaryimages/images/20251217-193545.png)

before the DllMain function:

![](https://isc.sans.edu/diaryimages/images/20251217-193611.png)

This is something to take into account when performing static analysis: next to looking at DllMain and exported functions, look also at TLS callbacks (if any).

And it's also important when performing dynamic analysis: when using a debugger, make sure to check how it is configured:

![](https://isc.sans.edu/diaryimages/images/20251217-194453.png)

This debugger is configured to break on TLS callbacks: thus these callbacks will not execute unbeknownst to you.

Didier Stevens

Senior handler

[blog.DidierStevens.com](http://blog.DidierStevens.com)
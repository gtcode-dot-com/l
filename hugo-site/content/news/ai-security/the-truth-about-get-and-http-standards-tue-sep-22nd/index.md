---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-10-04T23:42:06.932317+00:00'
exported_at: '2026-10-04T23:42:08.723629+00:00'
feed: https://isc.sans.edu/rssfeed.xml
language: en
source_url: https://isc.sans.edu/diary/rss/33358
structured_data:
  about: []
  author: ''
  description: 'The Truth about GET and HTTP Standards, Author: Johannes Ullrich'
  headline: The Truth about GET and HTTP Standards, (Tue, Sep 22nd)
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://isc.sans.edu/diary/rss/33358
  publisher:
    logo: /favicon.ico
    name: GTCode
title: The Truth about GET and HTTP Standards, (Tue, Sep 22nd)
updated_at: '2026-10-04T23:42:06.932317+00:00'
url_hash: 10cc5a04310895e03b4993ff45c539c3ed66f8df
---

On Friday, Xavier talked about the newly introduced
[HTTP Query](https://isc.sans.edu/diary/HTTP%20QUERY%20Method%3A%20The%20Grey%20Zone%20Between%20GET%20And%20POST./33352)
method. This new method was introduced to allow "GET" requests that include a body. The main reason for this was that GET requests typically do not contain a body. But what if they do?

The HTTP RFCs had "issues" defining this properly. RFC2616, which originally defined HTTP 1.1, stated in section 4.3:

&gt; A message-body MUST NOT be included in a request if the specification of the request method (section
&gt; [5.1.1](https://www.w3.org/Protocols/rfc2616/rfc2616-sec5.html#sec5.1.1)
&gt; ) does not allow sending an entity-body in requests.

And the GET specification never discussed message bodies.

This was somewhat reworded in the newer version, RFC 7231, section 4.3.2:

&gt; ??????A payload within a GET request message has no defined semantics; sending a payload body on a GET request might cause some existing implementations to reject the request.

I did a quick check of a couple of common web servers I had handy, to see what would happen:

### Apache

For this test, I ran Apache 2.4.68 on a Mac. It happily accepted a body with a GET request:

&gt; ```
&gt; % nc -c localhost 8080
&gt; GET /cgi-bin/test-cgi HTTP/1.1
&gt; Host: localhost
&gt; Content-Length: 6
&gt;
&gt; TEST
&gt; HTTP/1.1 200 OK
&gt; Date: Tue, 22 Sep 2026 14:39:17 GMT
&gt; Server: Apache/2.4.68 (Unix)
&gt; Transfer-Encoding: chunked
&gt; Content-Type: text/plain; charset=iso-8859-1
&gt;
&gt; 18a
&gt; CGI/1.0 test script report:
&gt; [some details omited]
&gt; CONTENT_LENGTH = 6
&gt; BODY = TEST
&gt; ```

The data was collected using a slightly modified version of the standard "test-cgi" script. The body was received just fine, and a 200 status was returned.

### NGINX

&gt; `% nc -c 10.128.1.11 80
&gt;
&gt; GET /cgi-bin/test-cgi HTTP/1.1
&gt;
&gt; Host: localhost
&gt;
&gt; Content-Length: 6`
&gt;
&gt; `TESTHTTP/1.1 301 Moved Permanently
&gt;
&gt; Server: nginx`

The request still did not trigger an error. But the body was ignored. The server started sending the response as soon as it received the headers. The body was ignored.

### Python

A simple Python web server (python -m http.server 8000) appears to behave just like NGINX. The body is ignored, but a response is sent back, and the status code is 200.

### Node

Node also ignores the Content-Length header and processes the request without error.

### lighthttpd

lighttpd/1.4.74 will return a 400 error and refuse to process the request.

### Java/Tomcat

Tomcat ignores the Content-Length header but returns a 200 response.

Do you have any web servers to test to see how they respond to a GET request with a body?

--

Johannes B. Ullrich, Ph.D. , Dean of Research,
[SANS.edu](https://sans.edu)

[Twitter](https://jbu.me/164)
|
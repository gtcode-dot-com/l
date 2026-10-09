---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-10-07T04:14:37.860510+00:00'
exported_at: '2026-10-07T04:14:45.975073+00:00'
feed: https://blog.trailofbits.com/feed/
language: en
source_url: https://blog.trailofbits.com/2026/10/02/sequencehash-multihashing-for-the-rest-of-us
structured_data:
  about: []
  author: ''
  description: We're releasing SequenceHash and its sister function SequenceMAC, a
    pair of related hash constructions that bring secure multihashing to developers
    using hash functions other than Keccak.
  headline: 'SequenceHash: multihashing for the rest of us'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://blog.trailofbits.com/2026/10/02/sequencehash-multihashing-for-the-rest-of-us
  publisher:
    logo: /favicon.ico
    name: GTCode
title: 'SequenceHash: multihashing for the rest of us'
updated_at: '2026-10-07T04:14:37.860510+00:00'
url_hash: ea8828624c8ac3cd8fcb5817357f5cbfcbdd297a
---

Multihashing is one of those cryptographic tasks that’s easy not to think about too much. This is unfortunate, because multihashing is a
[common stumbling point](/2024/08/21/yolo-is-not-a-valid-hash-construction/#yolomultihash)
when cryptographers try to use hashes.

As part of our goal to “fix software, not bugs,” Trail of Bits is introducing
[SequenceHash and its sister function SequenceMAC](https://github.com/C2SP/C2SP/blob/main/sequencehash.md)
, a pair of related hash constructions that bring secure multihashing to developers using hash functions other than Keccak. We hope SequenceHash and SequenceMAC will help cryptographers avoid attacks that take advantage of ambiguous input encodings. The specification is open source, and is now a
[part](https://github.com/C2SP/C2SP/blob/main/sequencehash.md)
of the Community Cryptography Specification Project (C2SP).

SequenceHash and SequenceMAC behave similarly to NIST’s
[TupleHash](https://csrc.nist.gov/pubs/sp/800/185/final)
, but have the advantage of not being tied to a single hash function. They also don’t require developers to implement fiddly computations that aren’t byte-aligned. Instead, SequenceHash and SequenceMAC work out of the box with nearly any secure cryptographic hash function you care to use, including SHA256/384/512, BLAKE, and RIPEMD. SequenceMAC supports keys 32 bytes or longer (up to the ridiculous limit of ${2}^{128}-1$ bytes).

(It’s worth noting: SequenceHash and SequenceMAC rely on the security of the underlying hash for their own security. SequenceHash and SequenceMAC can’t magically make MD4 or SHA0 secure again. For the purposes of this document, it’s assumed that you have chosen a reasonable hash function like SHA256, not CRC32.)

To make SequenceHash and SequenceMAC easy to use, we’re releasing three initial implementations of SequenceHash and SequenceMAC: one each in Rust, Go, and Python. We’re also releasing a large set of test vectors that cover multiple hash functions and include intermediate values to help developers debug and verify their implementations.

## Wait, “multihashing”?

Yeah, it’s a weird term, but the idea is pretty simple. “Multihashing” means “hashing a bunch of values together.” If you’ve ever read a cryptography paper, and there’s a step that says something like “compute the shared authenticator
`N=Hash(X, Y, Z, A, B)`
,” that’s multihashing. You need to create a hash that incorporates the inputs
`X, Y, Z, A`
, and
`B`
. Unfortunately, the simple “solution” of concatenating the inputs and hashing the result can lead to serious security problems.

For example, consider what happens when you hash three inputs using “raw” SHA256:

```
import hashlib

hasher = hashlib.new('sha256')
hasher.update(b'Test 0')
hasher.update(b'Test 1')
hasher.update(b'Test 2')
print(hasher.hexdigest())
hasher = hashlib.new('sha256')
hasher.update(b'Test 0Test 1')
hasher.update(b'Test 2')
print(hasher.hexdigest())
hasher = hashlib.new('sha256')
hasher.update(b'Test 0')
hasher.update(b'')
hasher.update(b'Test 1Test 2')
print(hasher.hexdigest())
```

This produces the following output:

```
4fce0a9940a42b5c9d1bcbfc9a6ddd6de20d731d584a0acf5bda6de86483641c
4fce0a9940a42b5c9d1bcbfc9a6ddd6de20d731d584a0acf5bda6de86483641c
4fce0a9940a42b5c9d1bcbfc9a6ddd6de20d731d584a0acf5bda6de86483641c
```

Even though inputs are fed in through separate calls, they’re not separated from the perspective of the hash function—under the hood, the inputs are just concatenated.

As with many things in cryptography, multihashing is harder than you think. That’s a big problem because multihashing is a critical component of one of the most important tools in zero-knowledge proofs: the
[Fiat-Shamir transform](/2021/02/19/serving-up-zero-knowledge-proofs/)
. When you get multihashing wrong, you introduce the risk of forgeries into your zero-knowledge proofs. Given that zero-knowledge proofs play a major role in cryptocurrency nowadays, that sort of mistake is sometimes measured in millions of dollars.

But Fiat-Shamir transforms aren’t the only place where you might want to use multihashing. It’s not uncommon to need to hash a collection of related objects, where both the objects
*and*
the collection are variable in size. Think of authenticating the files in an archive, grouping multiple cryptocurrency transactions into a single hash, or hashing something as
[“simple” as somebody’s name](https://www.kalzumeus.com/2010/06/17/falsehoods-programmers-believe-about-names/)
.

Multihashing is also used when generating cryptographic commitments to values. In some protocols, one party must perform calculations using secret values, only to reveal them to other parties for later verification. Often, this is done by hashing the secret value along with a random “blinding” value and broadcasting the result to other parties as the commitment. If the boundary between the secret value and the blinding value isn’t clear, a “commitment” can sometimes be opened several different ways.

Unfortunately, nobody seems to have landed on a consistent, standard solution to this problem. Instead, across the open-source ecosystem and in our private audits, we find developers solving the problem in wildly different ways. Some of these solutions are insecure, like using separator characters that can also appear in the inputs. Others encode their data in a way that makes their separators unambiguous, but the encoding is unnecessarily complex and introduces subtle timing risks. Think of stuff like Base64-encoding byte strings and separating the results with dollar signs. We often see situations where
*some*
hash inputs are length-encoded, but not
*all*
. It’s the wild west out there.

There are tools specific to Fiat-Shamir transforms, like
[Merlin](https://merlin.cool/)
and our own
[decree](https://github.com/trailofbits/decree)
, but they don’t work so well for
*general*
multihashing.

The most widely known standard for multihashing is TupleHash, defined in
[NIST SP 800-185](https://csrc.nist.gov/pubs/sp/800/185/final)
. To be clear, TupleHash is great. It solves the multihashing problem in a straightforward way (length-prefix encoding), and it handles inputs of
*effectively*
unlimited size (if you’re regularly hashing more than ${2}^{2040}-1$ bits of input, Trail of Bits wants to party with you and your disrespect for physics). As a bonus, it naturally operates as an XOF. If TupleHash is available for you, it’s a
*great*
tool.

TupleHash has a downside, though: it’s only defined to work with Keccak, the function that underpins SHA3. If you replace Keccak with another hash function, several of the important security features (like length-extension resistance) can go away. If you don’t have a Keccak implementation handy, you’re out of luck. Given that SHA3 and Keccak adoption have been pretty lackluster over the last decade, that leaves a lot of cryptographers out in the cold. This is especially true in the government contracting sector, where
[CNSA 2.0](https://media.defense.gov/2025/May/30/2003728741/-1/-1/0/CSA_CNSA_2.0_ALGORITHMS.PDF)
has mandated SHA384 and SHA512 for nearly everything.

This is a problem that cries out for a standardized solution. It calls for a complete specification. It begs for ready-to-use implementations available in multiple languages.

## Enter SequenceHash

SequenceHash is a hash-agnostic multihashing construct, similar to the way HMAC is a hash-agnostic MAC construct. You can use SequenceHash with your favorite hash functions, including the entire SHA2 family, BLAKE, RIPEMD, and more.

## What does SequenceHash offer?

SequenceHash offers four key features that prevent your hashed values from being mixed, extended, or replayed across contexts.

### Unambiguous input encoding

Given two inputs $\left({A,\ B}\right)$, you are guaranteed that there is no other sequence of inputs $\left({{I}\_{1},\ldots ,{I}\_{t}}\right)$, for any length $t$, that will result in the same input to the underlying hash function.

In other words, the values you hash are guaranteed to be “semantically distinct.” There’s no chance of playing games with the beginnings and endings of inputs, and there’s no opportunity to mix up parts of $A$ with $B$ or vice versa.

SequenceHash helps cryptographers follow
[the Horton principle](https://en.wikipedia.org/wiki/Horton_principle)
: you are hashing what you mean, and meaning what you hash.

### Length-extension prevention

Several popular hash functions, including SHA256 and SHA512, are vulnerable to length extension attacks. If Alice has a secret value $A$ and sends $H\left({A}\right)$ to Bob, then Bob can craft a value $B$ such that he can compute $H\left({A||B}\right)$, even though he doesn’t know $A$.

SequenceHash doesn’t have that issue. It uses a double-hash construction that prevents Bob from learning the information he needs to compute $H\left({A||B}\right)$.

### Built-in customization strings

If you’re developing cryptographic protocols, it’s often important to bind hashed values to a particular step in the protocol, or to a specific
*instance*
of the protocol, in order to prevent replay attacks or other problems related to reusing values.

SequenceHash makes this easy with built-in customization strings. Assuming you’re using a good hash function, applying SequenceHash or SequenceMAC to the same inputs with different customization strings will lead to unrelated outputs, allowing you to easily and predictably bind your hashes to particular uses. If you don’t need a customization string, don’t worry. They’re completely optional.

As an added bonus, the customization strings are incorporated only into the outer layer of the double-hash construction. If you need to hash the same value with multiple customization strings, the inner hash can be reused!

### MAC mode

One final cool feature of SequenceHash is that it has a keyed mode, SequenceMAC. SequenceMAC is structurally similar to HMAC, and offers the same features as SequenceHash: unambiguous encoding, customization strings, and length-extension protection. It also incorporates metadata about the key and customization strings to prevent the key pseudocollision issues present in HMAC.

## How does SequenceHash work?

Like TupleHash, SequenceHash uses length encoding to unambiguously encode its inputs. However, SequenceHash uses a simplified encoding. Instead of writing the number of bits to be hashed as a variable-length integer, SequenceHash encodes the number of bytes into a fixed-length, 128-bit integer. SequenceHash uses a length-suffix encoding for inputs. Like the length-prefix encoding system used by TupleHash, length-suffix encoding is unambiguous; however, suffix encoding allows implementers to develop streaming APIs when they need to support hashing data with length that isn’t known ahead of time.

We chose a 128-bit length encoding for simplicity of implementation on 32- and 64-bit systems (padding with zeroes is easy), and because a ${2}^{128}-1$ byte limit exceeds all practical considerations for the time being
*and*
the foreseeable future. Two of the most popular hash functions in use today, SHA256 and SHA512, limit their inputs to ${2}^{61}$ and ${2}^{125}$ bytes, respectively, meaning that a ${2}^{128}-1$-byte limit exceeds the specified limits of the most popular underlying hash functions, anyway. If you’re pushing the edges of SequenceHash, you’ve already blown past the limits of SHA256 and SHA512.

We use byte counts for simplicity. Nearly all hashing today is performed in software on strings of 8-, 16-, 32-, or 64-bit values. Systems using non-byte-length strings are very rare nowadays, and we believe it should be up to implementers of such systems to provide their own byte padding if they want to use SequenceHash.

Like HMAC, SequenceHash uses a double-hash construction to prevent length extension attacks. This structure also allows us to support a keyed variant, SequenceMAC, which accepts keys up to ${2}^{128}-1$ bytes in length.

One downside of the original HMAC construction is that it’s subject to what are known as “key pseudocollisions.” HMAC keys can be any length, but if they’re longer than a certain cutoff value (that depends on the hash), they get hashed before use. This means that every “long” key has a “short” representation that produces the exact same outputs. If you’re careful about specifying and enforcing key lengths in protocols, you can guard against this sort of problem, but if you’re not careful, somebody could present two versions of the “same” key in different contexts, allowing them to engage in shenanigans.

Another form of key pseudocollision is key extension. As far as HMAC is concerned, the 8-bit key
`0xff`
is the same as the 16-bit key
`0xff00`
and the 128-bit key
`0xff000000000000000000000000000000`
. Appending zeroes to a key doesn’t actually change it (unless it goes beyond the length cutoff, at least). This sort of pseudocollision is a bit more insidious, because it’s the sort of thing that can show up accidentally; it’s not hard to imagine unintentionally passing a 128-bit key instead of a 256-bit key, or incorrectly setting a length indicator somewhere.

The keyed variant of SequenceHash, SequenceMAC, incorporates key lengths into a header block that is part of the hash. As a result, HMAC-style long-key pseudocollisions are hard to find: if a key needs to be preprocessed by hashing, supplying the hash of the raw key is
*not*
the same as supplying the raw key. Trailing zeroes in a SequenceMAC key are semantically significant.

SequenceHash and SequenceMAC support customization strings for domain separation, similar to TupleHash’s customization strings. Customization strings can be up to ${2}^{128}-1$ bytes in length, and they’re only integrated into the
*outer*
hash function, allowing developers to derive multiple hashes from the same set of inputs
*without*
rehashing everything.

## How do I use it?

Glad you asked! We already have three implementations available:
[Rust](https://github.com/trailofbits/sequencehash-rs)
,
[Go](https://github.com/trailofbits/sequencehash-go)
, and
[Python](https://github.com/trailofbits/sequencehash-py)
. We also have a
[specification](https://c2sp.org/sequencehash)
available as part of the C2SP, with
[test vectors](https://github.com/C2SP/CCTV/tree/main/sequencehash)
available in case you want to write your own implementation.

The main feature that distinguishes the SequenceHash API from other APIs is that all updates to SequenceHash and SequenceMAC objects are
*atomic*
. That is, each time you write a value to a hashing object, it will be added to the hash as an independent, length-encoded object.

We have worked to make sure that the SequenceHash and SequenceMAC APIs are similar, but not identical, to the standard APIs for each language. The Go cryptographic library’s
`hash.Hash`
interface incorporates the
`io.Writer`
interface, which guarantees that writing two values in sequence is the same as writing their concatenation. The Python hash library makes similar guarantees for the PEP 247
`update`
function.

Let’s see what happens when we hash our example values above using SequenceHash:

```
import sequencehash

hasher = sequencehash.SequenceHash.new('sha256')
hasher.add(b'Test 0')
hasher.add(b'Test 1')
hasher.add(b'Test 2')
print(hasher.result().hex())
hasher = sequencehash.SequenceHash.new('sha256')
hasher.add(b'Test 0Test 1Test 2')
print(hasher.result().hex())
hasher = sequencehash.SequenceHash.new('sha256')
hasher.add(b'Test 0')
hasher.add(b'Test 1Test 2')
print(hasher.result().hex())
```

We get the following output:

```
6eea7264b266d35bd5e483ef042189d2cebe51f9e8b764b90b0f9c82185de7ca
1469d91e90c1d9c6189f576822e900f5cc8c3cdbd2ec51256df649d37c1688f7
1800a2188e126c79dac8f7cf7e38a66e3f797654c15a5e49248a94d4e99bcaae
```

The three outputs are all unrelated. That’s because each of the inputs is length-encoded, meaning that feeding
`Test 0`
and
`Test 1`
into consecutive calls to SequenceHash is
*not*
the same as feeding
`Test 0Test 1`
into a single call.

We can also try hashing identical inputs with different customization strings:

```
import sequencehash

hasher = sequencehash.SequenceHash.new('sha256')
hasher.add(b'Test 0')
print(hasher.result_with_customizer(b'CUST 0').hex())

hasher = sequencehash.SequenceHash.new('sha256')
hasher.add(b'Test 0')
print(hasher.result_with_customizer(b'CUST 1').hex())

hasher = sequencehash.SequenceHash.new('sha256')
hasher.add(b'Test 0')
print(hasher.result_with_customizer(b'CUST 2').hex())
```

Again, we have three unrelated outputs:

```
3e54b5cd60ef78773dcf14c5f65ed593726a981f2c80045db7fac03015cc07ad
3c5b12ea6952714fed499796a743b103de97575fc938aab7d154cc6c605984a9
706af798b32b12c9f508c16c3411b594227f79936a3cc521e6e1f362b1ef3a38
```

## Sounds cool. What about SequenceMAC?

SequenceMAC works like SequenceHash, but with a 32-byte or longer key. As with SequenceHash, we can see that shifting the boundaries between our inputs leads to different results:

```
import sequencehash

KEY = bytes.fromhex("c5d6670f20adad622292a404dc5496cd6692fee636b5935a18451c985b7277bc9cacbc26e5473f85cfc6a64e96d0b98e7b9b604eaebc8899971e1a97dc3caa3a")

hasher = sequencehash.SequenceMAC.new(KEY, digestmod='sha256')
hasher.add(b'Test 0')
hasher.add(b'Test 1')
print(hasher.result().hex())

hasher = sequencehash.SequenceMAC.new(KEY, digestmod='sha256')
hasher.add(b'Test 0Test 1')
print(hasher.result().hex())

hasher = sequencehash.SequenceMAC.new(KEY, digestmod='sha256')
hasher.add(b'Test 0')
hasher.add(b'')
hasher.add(b'Test 1')
print(hasher.result().hex())
```

This gives us the following output:

```
9a24e4209dad98d2e1f1eecd62aa2908234f1eed2963395292fd9718129fe258
4e4b71b8bb7b2c80e9f9ca89cb8bff43cd77cc5b530fc5f163069e5dda2876cb
6faf7818842f5a208dc306afe83ed7bea5b3fadc2a617c2208e836709f925889
```

Changing the key, or using
`result_with_customizer`
with different customization values, will also provide different outputs.

### Some notes on key size

One important point is that SequenceMAC has a
*minimum*
key size of 32 bytes (256 bits). Coupled with a good 256-bit hash function, this corresponds to about a 128-bit security level against forgery attacks. As with HMAC, key sizes should generally be at least as long as the output of the hash.

Additionally, while SequenceMAC supports keys up to ${2}^{128}-1$ bytes in length, it’s important to remember that “longer key” is not the same as “higher security.” The underlying hash function and the key-preprocessing step (which hashes keys longer than the underlying hash function’s block size) impose a hard cap on the total security SequenceMAC can provide. Using keys longer than the length of the hash output is generally not a good idea.

For hash functions with outputs smaller than 256 bits (such as SHA224 or RIPEMD160), the security level should be equal to about half the hash length (112 bits for SHA224 and 80 bits for RIPEMD160), which does not match the security of the minimum key size. While SequenceMAC can be used with such hash functions, the SequenceMAC specification only
*prohibits*
short keys and
*strongly discourages*
the use of hash functions with short outputs.

## What about extensible output functions (XOFs)?

Excellent question! We don’t have an answer yet!

We haven’t specified SequenceXOF, but it’s definitely something we’re thinking about. Right now, XOFs aren’t as widely used as hashes, so the APIs are a little less stable. We want to proceed carefully to ensure we cover all the relevant use cases.

## What if I want to write my own implementation?

We love to see high-quality implementations! There are many languages where someone might find SequenceHash and SequenceMAC useful, and there are certainly ways to customize the current APIs to better fit your needs!

First,
[check out the specification](https://github.com/C2SP/C2SP/blob/main/sequencehash.md)
. The document is kinda long, but the structure is straightforward. If you’ve implemented HMAC before, SequenceHash and SequenceMAC will feel like fancy versions of that.

Second, if your target language is similar to Rust, Go, or Python, consider porting over our initial implementations. We’ve tried to keep these implementations as clean as we can, so they’re easy to audit and other cryptographers can learn from them.

Finally, whatever you do, don’t forget to check your implementation against the
[test vectors](https://github.com/C2SP/CCTV/tree/main/sequencehash)
. The test vectors aren’t simple known-answer tests, either: they include intermediate values that can be used to help debug and validate your implementation.

## Some minor caveats

SequenceHash provides for a specific set of needs: customization and domain separation, preventing length extension attacks where applicable, and—most importantly—ensuring that your inputs don’t get mixed together in a dangerous way. It’s a tool, not a panacea.

You still need to make sure you’re hashing
*the right*
inputs. Being able to decode a value doesn’t mean that two pieces of software will encode that value in
*the same way*
, and that can lead to compatibility issues among different servers, clients, and libraries. JSON and XML, for instance, don’t always guarantee field orderings. Even for strings, it’s important to make sure you’re using a consistent encoding method (“all the world is ASCII” isn’t true and never has been).

In the case of Fiat-Shamir transforms, you still have to be careful about
[including
*all*
your inputs](https://eprint.iacr.org/2023/691)
. Schnorr proofs should always include the group descriptor (whether as individual values or named parameter sets), the generator element, etc. When the output is supposed to be interpreted as an integer modulo some other value, it’s also important to make sure that you select a hash with an output large enough to avoid modulo bias. Cryptography is subtle; there are always intricacies to consider.

Still, as long as you’re careful to keep your inputs consistent and include all your values, SequenceHash and SequenceMAC make it easy to ensure nobody can pretend your inputs mean something other than what they’re supposed to mean.

The specification is live at C2SP, and our Rust, Go, and Python implementations are ready to use today, with test vectors available if you want to write your own. Try it out and let us know what you think!
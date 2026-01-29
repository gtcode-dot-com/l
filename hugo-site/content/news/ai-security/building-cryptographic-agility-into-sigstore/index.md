---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-01-29T12:15:13.905251+00:00'
exported_at: '2026-01-29T12:15:16.949167+00:00'
feed: https://blog.trailofbits.com/feed/
language: en
source_url: https://blog.trailofbits.com/2026/01/29/building-cryptographic-agility-into-sigstore
structured_data:
  about: []
  author: ''
  description: "\n                We collaborated with the Sigstore community to build
    cryptographic agility into the software signing ecosystem, enabling organizations
    to use different signing algorithms while maintaining security through predefined
    algorithm suites and out-of-band configuration rather than dangerous in-band signaling.\n
    \           "
  headline: Building cryptographic agility into Sigstore
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://blog.trailofbits.com/2026/01/29/building-cryptographic-agility-into-sigstore
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Building cryptographic agility into Sigstore
updated_at: '2026-01-29T12:15:13.905251+00:00'
url_hash: 5320677fd1cf086351eb4ddc58b49e0dbee533b4
---

Software signatures carry an invisible expiration date. The container image or firmware you sign today might be deployed for 20 years, but the cryptographic signature protecting it may become untrustworthy within 10 years. SHA-1 certificates become worthless, weak RSA keys are banned, and quantum computers may crack today’s elliptic curve cryptography. The question isn’t whether our current signatures will fail, but whether we’re prepared for when they do.

Sigstore, an open-source ecosystem for software signing, recognized this challenge early but initially chose security over flexibility by adopting new cryptographic algorithms as older ones became obsolete. By hard coding ECDSA with P-256 curves and SHA-256 throughout its infrastructure, Sigstore avoided the dangerous pitfalls that have plagued other crypto-agile systems. This conservative approach worked well during early adoption, but as Sigstore’s usage grew, the rigidity that once protected it began to restrict its utility.

Over the past two years, Trail of Bits has collaborated with the Sigstore community to systematically address the limitations of aging cryptographic signatures. Our work established a centralized algorithm registry in the Protobuf specifications to serve as a single source of truth. Second, we updated Rekor and Fulcio to accept configurable algorithm restrictions. And finally, we integrated these capabilities into Cosign, allowing users to select their preferred signing algorithm when generating ephemeral keys. We also developed Go implementations of post-quantum algorithms LMS and ML-DSA, demonstrating that the new architecture can accommodate future cryptographic standards. Here is what motivated these changes, what security considerations shaped our approach, and how to use the new functionality.

## Sigstore’s cryptographic constraints

Sigstore hard codes ECDSA with P-256 curves and SHA-256 throughout most of its ecosystem. This rigidity is a deliberate design choice. From Fulcio certificate issuance to Rekor transparency logs to Cosign workflows, most steps default to this same algorithm. Cryptographic agility has historically led to serious security vulnerabilities, and focusing on a limited set of algorithms reduces the chance of something going wrong.

This conservative approach, however, has created challenges as the ecosystem has matured. Various organizations and users have vastly different requirements that Sigstore’s rigid approach cannot accommodate. Here are some examples:

* **Compliance-driven organizations**
  might need NIST-standard algorithms to meet regulatory requirements.
* **Open-source maintainers**
  may want to sign artifacts without making cryptographic decisions, relying on secure defaults from the public Sigstore instance.
* **Security-conscious enterprises**
  may want to deploy internal Sigstore instances using only post-quantum cryptography.

Furthermore, software artifacts remain in use for decades, meaning today’s signatures must stay verifiable far into the future, and the cryptographic algorithm used today might not be secure 10 years from now.

These challenges can be addressed only if Sigstore allows for a certain degree of cryptographic agility. The goal is to enable controlled cryptographic flexibility without repeating the security issues that have affected other crypto-agile systems. To address this, the Sigstore community has developed a
[design document](https://docs.google.com/document/d/18vTKFvTQdRt3OGz6Qd1xf04o-hugRYSup-1EAOWn7MQ/edit?tab=t.0#heading=h.op2lvfrgiugr)
outlining how to introduce cryptographic agility while maintaining strong security guarantees.

## The dangers of cryptographic flexibility

The most infamous example of problems caused by cryptographic flexibility is
[the JWT](https://jwt.io/introduction)
`alg:`
`none`
vulnerability, where some JWT libraries treated tokens signed with the
`none`
algorithm as valid tokens, allowing anyone to forge arbitrary tokens and “sign” whatever payload they wanted. Even more subtle is the
[RSA/HMAC confusion attack in JWT](https://portswigger.net/web-security/jwt/algorithm-confusion)
, where a mismatch between what kind of algorithm a server expects and what it receives allows anyone with knowledge of the RSA public key to forge tokens that pass verification.

The fundamental problem in both cases is in-band algorithm signaling, which allows the data to specify how it should be protected. This creates an opportunity for attackers to manipulate the algorithm choice to their advantage. As the cryptographic community has learned through painful experience, cryptographic agility introduces significant complexity, leading to more code and increased potential attack vectors.

## The solution: Controlled cryptographic flexibility

Instead of allowing users to mix and match any algorithms they want, Sigstore introduced predefined algorithm suites, which are complete packages that specify exactly which cryptographic components work together.

For example,
`PKIX_ECDSA_P256_SHA_256`
not only includes the signing algorithm (ECDSA P-256), but also mandates SHA-256 for hashing. A
`PKIX_ECDSA_P384_SHA_384`
suite pairs ECDSA P-384 with SHA-384, and
`PKIX_ED25519`
uses Ed25519 and SHA-512. Users can choose between these suites, but they can’t create dangerous combinations, such as ECDSA P-384 with MD5.

Critically, the choice of which algorithm to use comes from out-of-band negotiation, meaning it’s determined by configuration or policy, not by the data being signed. This prevents the in-band signaling attacks that have plagued other systems.

## The implementation

To enable cryptographic agility across the Sigstore ecosystem, we needed to make coordinated changes that would work together seamlessly. Cryptography is used in several places within the Sigstore ecosystem; however, we primarily focused on enabling clients to change the signing algorithm used to sign and verify artifacts, as this would have a significant impact on end users. We tackled this change in three phases.

### Phase 1: Establishing common ground

We introduced a centralized
[algorithm registry](https://github.com/sigstore/protobuf-specs/blob/966b43d006e7fc938b30724933af34c8e351f2a1/protos/sigstore_common.proto#L46-L129)
in the Protobuf specifications that defines all
[allowed algorithms](https://github.com/sigstore/sigstore/blob/1e63a2159e71d968a5fa46215280103844797ee8/pkg/signature/algorithm_registry.go#L154)
and their details. We also implemented
[default mappings](https://github.com/sigstore/sigstore/blob/1e63a2159e71d968a5fa46215280103844797ee8/pkg/signature/algorithm_registry.go#L238-L298)
from key types to signing algorithms (e.g., ECDSA P-256 keys automatically use ECDSA P-256 + SHA-256), eliminating ambiguity and providing a single source of truth for all Sigstore components.

### Phase 2: Service-level updates

We updated
[Rekor](https://github.com/sigstore/rekor/pull/1974)
and
[Fulcio](https://github.com/sigstore/fulcio/pull/1938)
with a new
`--client-signing-algorithms`
flag that lets deployments specify which algorithms they accept, enabling custom restrictions like Ed25519-only or future post-quantum-only deployments. We also
[fixed Fulcio](https://github.com/sigstore/fulcio/pull/1959)
to use proper hash algorithms for each key type (SHA-384 for ECDSA P-384, etc.) instead of defaulting everything to SHA-256.

### Phase 3: Client integration

We updated Cosign to support multiple algorithms by
[removing hard-coded SHA-256](https://github.com/sigstore/cosign/pull/4050)
usage and adding a
[`--signing-algorithm`](https://github.com/sigstore/cosign/pull/3497)
flag for generating different ephemeral key types. Currently available in
`cosign sign-blob`
and
`cosign verify-blob`
, these changes let users bring their own keys of any supported type and easily select their preferred cryptographic algorithm when ephemeral keys are used. Other clients implementing the Sigstore specification can choose which set of algorithms to use, as long as it is a subset of the allowed algorithms listed in the algorithm registry.

### Validation: Proving it works

To demonstrate the flexibility of our new architecture, we developed HashEdDSA (Ed25519ph) support in both
[Rekor](https://github.com/sigstore/rekor/pull/1945)
and
[the Sigstore Go library](https://github.com/sigstore/sigstore/pull/1595)
and created Go implementations of post-quantum algorithms
[LMS](https://github.com/trailofbits/lms-go)
and
[ML-DSA](https://github.com/trailofbits/ml-dsa)
. This work proved that our modular architecture can accommodate diverse cryptographic algorithms and provides a solid foundation for future additions, including post-quantum cryptography.

## Cryptographic flexibility in action

Let’s see this cryptographic flexibility in action by setting up a custom Sigstore deployment. We’ll configure a private Rekor instance that accepts only ECDSA P-521 with SHA-512 and RSA-4096 with SHA-256, by using the
`--client-signing-algorithms`
flag, demonstrating both algorithm restriction and the new Cosign capabilities.

```
~/rekor$ git diff
diff --git a/docker-compose.yml b/docker-compose.yml
index 3e5f4c3..93e0d10 100644
--- a/docker-compose.yml
+++ b/docker-compose.yml
@@ -120,6 +120,7 @@ services:
       "--enable_stable_checkpoint",
       "--search_index.storage_provider=mysql",
       "--search_index.mysql.dsn=test:zaphod@tcp(mysql:3306)/test",
+      "--client-signing-algorithms=ecdsa-sha2-512-nistp521,rsa-sign-pkcs1-4096-sha256",
       # Uncomment this for production logging
       # "--log_type=prod",
       ]

$ docker compose up -d
```

Let’s create the artifact and use Cosign to sign it:

```
$ echo "Trail of Bits & Sigstore" > msg.txt
$ ./cosign sign-blob --bundle cosign.bundle --signing-algorithm=ecdsa-sha2-512-nistp521 --rekor-url http://localhost:3000 msg.txt
Retrieving signed certificate...
Successfully verified SCT...
Using payload from: msg.txt
tlog entry created with index: 111111111
Wrote bundle to file cosign.bundle
qzbCtK4WuQeoeZzGP1111123+...+j7NjAAAAAAAA==
```

This last command performs a few steps:

1. Generates an ephemeral private/public ECDSA P-521 key pair and gets the SHA-512 hash of the artifact (
   `--signing-algorithm=ecdsa-sha2-512-nistp521`
   )
2. Uses the ECDSA P-521 key to request a certificate to Fulcio
3. Signs the hash with the certificate
4. Submits the artifact’s hash, the certificate, and some extra data to our local instance of Rekor (
   `--rekor-url http://localhost:3000`
   )
5. Saves everything into the
   `cosign.bundle`
   file (
   `--bundle cosign.bundle`
   )

We can verify the data in the bundle to ensure ECDSA P-521 was actually used (with the right hash function):

```
$ jq -C '.messageSignature' cosign.bundle
{
  "messageDigest": {
    "algorithm": "SHA2_512",
    "digest": "WIjb9UuEBgdSxhRMoz+Zux4ig8kWY...+65L6VSPCKCtzA=="
  },
  "signature": "MIGIAkIBRrn.../zgwlBT6g=="
}

$ jq -r '.verificationMaterial.certificate.rawBytes' cosign.bundle | base64 -d  | openssl x509 -text -noout -in /dev/stdin | grep -A 6 "Subject Public Key Info"
        Subject Public Key Info:
            Public Key Algorithm: id-ecPublicKey
                Public-Key: (521 bit)
                pub:
                    04:01:36:90:6c:d5:53:5f:8d:4b:c6:2a:13:36:69:
                    31:54:e3:2d:92:e0:bd:d5:77:35:37:62:cd:6a:4d:
                    9f:32:83:97:a7:0d:4e:48:73:fe:3c:a2:0f:f2:3d:
```

Now let’s try a different key type to see if it’s rejected by Rekor. To generate a different key type, we just need to switch the value of
`--signing-algorithm`
in Cosign:

```
$ ./cosign sign-blob --bundle cosign.bundle --signing-algorithm=ecdsa-sha2-256-nistp256 --rekor-url http://localhost:3000 msg.txt
Generating ephemeral keys...
Retrieving signed certificate...
Successfully verified SCT...
Using payload from: msg.txt
Error: signing msg.txt: [POST /api/v1/log/entries][400] createLogEntryBadRequest {"code":400,"message":"error processing entry: entry algorithms are not allowed"}
error during command execution: signing msg.txt: [POST /api/v1/log/entries][400] createLogEntryBadRequest {"code":400,"message":"error processing entry: entry algorithms are not allowed"}
```

As we can see, Rekor did not allow Cosign to save the entry (
`entry algorithms are not allowed`
), as
`ecdsa-sha2-256-nistp256`
was not part of the list of algorithms allowed through the
`--client-signing-algorithms`
flag used when starting the Rekor instance.

## Future-proofing Sigstore

The changes that Trail of Bits has implemented alongside the Sigstore community allow organizations to use different signing algorithms while maintaining the same security model that made Sigstore successful.

Sigstore now supports algorithm suites from ECDSA P-256 to Ed25519 to RSA variants, with a centralized registry ensuring consistency across deployments. Organizations can configure their instances to accept only specific algorithms, whether for compliance requirements or post-quantum preparation.

The foundation is now in place for future algorithm additions. As cryptographic standards evolve and new algorithms become available, Sigstore can adopt them through the same controlled process we’ve established. Software signatures created today will remain verifiable as the ecosystem adapts to new cryptographic realities.

Want to dig deeper? Check out our
[LMS](https://github.com/trailofbits/lms-go)
and
[ML-DSA](https://github.com/trailofbits/ml-dsa)
Go implementations for post-quantum cryptography, or run
`--help`
on Rekor, Fulcio, and Cosign to explore the new algorithm configuration options. If you’re looking to modernize your project’s cryptography to current standards,
[Trail of Bits’ cryptography consulting services](https://www.trailofbits.com/services/cryptography)
can help you get on the right path.

We would like to thank Google, OpenSSF, and Hewlett-Packard for having funded some of this work. Trail of Bits continues to contribute to the Sigstore ecosystem as part of our ongoing commitment to strengthening open-source security infrastructure.
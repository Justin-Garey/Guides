# Certificates

## What are Certificates

Certificates provide identity validation and trust between two parties. For example, most websites run HTTPS or HTTP over SSL which provides a certificate from a known certificate authority to validate the website provides a trusted connection. 

## What is a Certificate Authority (CA)

A certificate authority (CA) is a trusted entity that can create certificates and cut new CAs. Comparing two certificates from the same CA will provide the validation that the other party can be trusted.

## Creating a Local CA

Generate the Certificate Authority key:

```bash
openssl genrsa -des3 -out CA.key 2048
```

- Enter a passphrase: e.g. "example"

Generate the Certificate Authority certificate:

```bash
openssl req -x509 -new -nodes -key CA.key -sha256 -days 100 -subj "/C=US/O=EX" -out CA.pem
```

## Creating a Key, Certificate Pair

Generate the key:

```bash
openssl genrsa -out K1.key 2048
```

Create a Certificate Signing Request (CSR) from the key:

```bash
openssl req -new -key K1.key -subj "/C=US/O=EX/CN=K1" -out K1.csr
```

- Change the CN to the name or id.

Sign the CSR with the CA:

```bash
openssl x509 -req -in K1.csr -CA CA.pem -CAkey CA.key -CAcreateserial -out K1.crt -days 100 -sha256
```

## Post Quantum Cryptography (PQC)

To handle the future of quantum computers breaking existing cryptography, PQC algorithms are being used instead.

- For post-quantum key exchange (confidentiality), Module-Lattice-Based Key-Encapsulation Mechanism (ML-KEM) or CRYSTALS-KYBER is being used.
- For post-quantum certificates (authentication), Module-Lattice-Based Digital Signature Algorithm (ML-DSA) or CRYSTALS-Dilithium is being used.
- For post-quantum digital signatures (integrity), Stateless Hash-Based Digital Signature Algorithm (SLH-DSA) or SPHINCS+ is being used.

To use PQC algorithms instead of the traditional algorithms, Linux devices with OpenSSL require versions greater than 3.5 with the algorithms built in.

## Resources

- [Cloudflare](https://www.cloudflare.com/learning/ssl/quantum/what-is-post-quantum-cryptography/) on PQC.
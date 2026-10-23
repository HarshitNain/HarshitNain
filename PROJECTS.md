# 🚀 Key Featured Projects — Harshit Nain

Detailed architectural analysis of production platforms, distributed microservices, and interactive modern web applications engineered by **Harshit Nain**.

---

## 1. ⚙️ GRC – Distributed Monolith
**Company / Organization:** RNR Consulting Pvt. Ltd.  
**Tech Stack:** Golang, gRPC, Protobuf, NATS JetStream, Kong API Gateway, PostgreSQL, React.js, TanStack Query

### Architecture & Overview
Architected a mission-critical production distributed system with modular domain boundaries, eliminating the operational overhead of fragmented deployments while retaining strict service decoupling.

### Key Engineering Achievements:
- **Low-Latency gRPC Messaging:** Implemented gRPC and Protobuf for strongly typed, binary-serialized inter-service communication with sub-millisecond serialization overhead.
- **Asynchronous Pub/Sub:** Integrated **NATS JetStream** for persistent, guaranteed message delivery and real-time event broadcasting, decoupling background workers from user request paths.
- **API Gateway & Protection:** Configured **Kong API Gateway** with JWT bearer token validation, custom rate-limiting tiers, and path routing to shield 20+ internal microservices.
- **Live Analytics Dashboard:** Built a real-time React analytics portal with **TanStack Query** server-state caching, synchronizing live operational metrics and reducing dashboard load times by 30%.

---

## 2. 🛡️ ARC – Automated Rights and Consents
**Company / Organization:** RNR Consulting Pvt. Ltd.  
**Tech Stack:** Golang, React.js, PostgreSQL, REST APIs, Docker, Apache Kafka, Redis, SMTP, HashiCorp Vault

### Architecture & Overview
Engineered an end-to-end data compliance and consent orchestration microservice built strictly in alignment with India's **Digital Personal Data Protection Act (DPDP Act)**.

### Key Engineering Achievements:
- **5+ Dynamic Consent Workflows:** Designed and shipped workflows for cookie consent management, grievance redressal tracking, data subject erasure requests, and verifiable parental consent.
- **Embeddable Client Widgets:** Authored lightweight, zero-dependency JavaScript client widgets that third-party partner portals can embed with a single `<script>` tag.
- **Audit-Proof Telemetry:** Implemented tamper-evident, append-only audit logging in PostgreSQL with Redis caching for rapid verification during regulatory audits.
- **Enterprise Security:** Integrated HashiCorp Vault for dynamic database credentials and cryptographic encryption of personal identifying information (PII).

---

## 3. 🍔 Food Villa
**Tech Stack:** React.js, Redux Toolkit, Swiggy API, Geolocation API, CSS3

### Architecture & Overview
Interactive online food ordering and restaurant discovery web application emphasizing component modularity, fluid user feedback, and accurate real-world data integration.

### Key Engineering Achievements:
- **Real-Time Geolocation Tracking:** Integrated the browser Geolocation API with reverse geocoding to automatically detect user delivery zones and fetch local active restaurants.
- **Dynamic Restaurant Filtering:** Engineered real-time client-side search, cuisine filters, top-rated sorting, and delivery time estimations via third-party Swiggy API endpoints.
- **Persistent Redux Cart:** Leveraged Redux Toolkit slices with local persistence to maintain cart items, custom notes, and user delivery preferences seamlessly across sessions.

---

## 4. 🛣️ NHIT Digital Platform
**Tech Stack:** Golang, PostgreSQL, Docker, Redis, REST APIs

### Architecture & Overview
Next-generation digital operating system designed for National Highways Infra Trust (NHIT) to manage multi-tier financial approvals, infrastructure toll assets, and banking reconciliation.

### Key Engineering Achievements:
- **Direct Banking UTR Reconciliation:** Automated direct host-to-host banking transaction verification with 100% matched UTR tracking.
- **Statutory Tax Automation:** Engineered automated Section 194C TDS calculation and deduction workflows, replacing manual spreadsheet reconciliation.
- **Sub-45ms API Latency:** Optimized concurrent Go request handlers with connection pooling and PostgreSQL index tuning.

---

## 5. 🏢 AppSquadz Core APIs & Modular UI Suite
**Company / Organization:** AppSquadz Pvt. Ltd.  
**Tech Stack:** Node.js, Express.js, React.js, Redux Toolkit, REST APIs

### Architecture & Overview
Core backend API infrastructure and multi-module frontend components powering enterprise business workflows and partner integrations.

### Key Engineering Achievements:
- **15+ Scalable RESTful Endpoints:** Designed, tested, and released robust Node.js/Express endpoints supporting high-throughput transaction loads.
- **Reusable UI Component System:** Built modular React component libraries used across 4+ product modules, maximizing accessibility and consistency.
- **State Standardization:** Centralized asynchronous data fetching with Redux Toolkit, eliminating state synchronization bugs and cutting UI/API integration errors by 20%.
- **Cross-Browser Hardening:** Audited and resolved edge-case rendering bugs across 30+ responsive screen resolutions.

---

## 6. 🔄 Enterprise SyncHub & 🛡️ Secure Gateway Shield
**Tech Stack:** Golang, WebSockets, Redis, Kong Gateway, JWT

### Architecture & Overview
High-concurrency synchronization gateway and security shield providing real-time bidirectional WebSocket event streams and hardened perimeter defenses.

### Key Engineering Achievements:
- **500+ Concurrent WebSocket Sessions:** Scaled connection brokers to handle persistent bidirectional message streams with zero dropped frames.
- **Rate-Limiting & Threat Shield:** Implemented token bucket rate-limiting algorithms to protect public microservice endpoints against brute-force abuse.

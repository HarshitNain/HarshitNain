# 📝 Technical Articles & Architecture Notes

---

## ⚙️ Systems Engineering & Platform Architecture

### 1. **Architecting the NHIT Digital Operating System: Sub-45ms P99 Latency with Go & PostgreSQL**
- **Tags:** #Go #SystemsArchitecture #HighThroughput #PostgreSQL
- **Summary:** A deep technical dive into engineering a national-scale highway infrastructure trust platform. Explores goroutine pooling, non-blocking I/O, database connection pool tuning, and query indexing strategies that consistently deliver sub-45ms response times.
- **Key Highlights:**
  - Concurrent batch ingestion with worker pools
  - Database schema normalization & partial indexing for high-frequency writes
  - Fault-tolerant gRPC and RESTful gateway integration

### 2. **Automating Host-to-Host Banking UTR Reconciliation & Statutory Tax Deductions (Section 194C)**
- **Tags:** #Fintech #Banking #Automation #TaxCompliance
- **Summary:** Eliminating manual banking reconciliations across expressway concessionaires. Covers automated Section 194C TDS calculation algorithms, multi-tier cryptographic sign-offs, and 100% verified UTR matching against core banking systems.
- **Key Highlights:**
  - Multi-tier financial approval state machines
  - Idempotent banking transaction execution
  - Automated anomaly detection for reconciliation mismatches

### 3. **Building Resilient Distributed In-Memory OTP Stores with Expiration Tracking in Go**
- **Tags:** #Go #Security #DistributedSystems #Redis
- **Summary:** Architectural considerations when designing high-security in-memory OTP stores. Covers atomic mutex-free TTL tracking, safe concurrency patterns, rate-limiting shields, and fallback persistence.
- **Key Highlights:**
  - Memory-safe key-value expiration algorithms
  - Anti-brute-force sliding window rate limiters
  - Cryptographic token generation and zero-leak memory sanitation

---

## 🌐 Modern Frontend & Cloud Engineering

### 4. **Predictable State Architecture: Scaling React with Redux Toolkit & Memoized Selectors**
- **Tags:** #React #ReduxToolkit #FrontendArchitecture #Performance
- **Summary:** Lessons from building complex e-commerce and food delivery platforms. How to organize Redux Toolkit slices, avoid unnecessary component re-renders with `createSelector`, and achieve 98/100 Lighthouse performance.
- **Key Highlights:**
  - Normalized state trees and entity adapters
  - Virtualized rendering for infinite lists
  - Code splitting and asset optimization in Docker containers

### 5. **This Profile is a Program: Self-Hosted Neubrutalist Telemetry with SVG & GitHub Actions**
- **Tags:** #GitHubActions #SVG #Automation #Telemetry
- **Summary:** How to build an automated, self-hosted developer telemetry dashboard that runs on daily GitHub Actions pipelines, generates dynamic SVG instruments from live GitHub API metrics, and renders zero-dependency interactive graphics.
- **Key Highlights:**
  - Pure SVG vector rendering with SMIL micro-animations
  - Neubrutalist and cyber-HUD design systems
  - Local JSON caching and offline rate-limit resilience

---

## 📬 Connect & Discuss

Want to discuss distributed architecture, Go systems, or web platforms?  
Reach out via **[Email](mailto:hnain932@gmail.com)** or explore the codebase on **[GitHub](https://github.com/HarshitNain)**.

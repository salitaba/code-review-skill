---
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
runs: 1
---

Review this change as you would review a pull request.

There is no repository to search. The files below are the complete relevant
context: one changed file, and two unchanged files included because they show
behavior the changed file participates in.

**Changed — `InvoiceLookupService.java`:**

```java
@Service
public class InvoiceLookupService {

    private final InvoiceRepository invoiceRepository;

    // CHANGED: read-only lookup used by the admin UI.
    @Transactional(readOnly = true)
    public Optional<Invoice> find(String invoiceId) {
        Optional<Invoice> invoice = invoiceRepository.findById(invoiceId);
        log.info("invoice lookup for {}", invoice.map(Invoice::getEmail).orElse("unknown"));
        return invoice;
    }
}
```

**Unchanged — `BillingService.java`:**

```java
@Service
public class BillingService {

    public void process(String invoiceId) {
        Invoice invoice = invoiceRepository.findById(invoiceId).orElseThrow();
        // The invoice email is already written to the application log here.
        log.info("processing invoice for {}", invoice.getEmail());
        ...
    }
}
```

**Unchanged — `InvoiceRepository.java`:**

```java
public interface InvoiceRepository extends JpaRepository<Invoice, String> {
    // Spring Data derives a parameterized query from the method name.
    Optional<Invoice> findById(String id);
}
```

Admin endpoints require an authenticated administrator. That is enforced in
unchanged security configuration which is not shown here.

Report findings using your normal review output and severity scale, and state your
review decision.

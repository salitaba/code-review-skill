---
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
runs: 1
---

Review this change as you would review a pull request.

There is no repository to search. The three files below are the complete relevant
context: one changed file, and two unchanged files included because they affect
the changed file's behavior.

**Changed — `LedgerService.java`:**

```java
@Service
public class LedgerService {

    private final LedgerRepository ledgerRepository;

    // CHANGED: transient database failures were dropping paid-order events,
    // so the write is now retried.
    @Retryable(retryFor = TransientDataAccessException.class, maxAttempts = 5)
    @Transactional
    public void record(OrderPaid event) {
        LedgerEntry entry = new LedgerEntry(event.orderId(), event.amount());
        ledgerRepository.save(entry);
    }
}
```

**Unchanged — `LedgerEventListener.java`:**

```java
@Component
public class LedgerEventListener {

    private final LedgerService ledgerService;

    // The topic is at-least-once; a broker redelivery after an unacked failure
    // is expected behavior, not an error.
    @KafkaListener(topics = "order-paid")
    public void on(OrderPaid event) {
        ledgerService.record(event);
    }
}
```

**Unchanged — `PriceCache.java`:**

```java
@Component
public class PriceCache {

    private volatile Map<String, BigDecimal> prices = Map.of();

    // Replaces the whole map; readers see either the previous map or the new one.
    @Scheduled(fixedDelay = 60_000)
    void refresh() {
        prices = loadFromDatabase();
    }

    public BigDecimal price(String sku) {
        return prices.get(sku);
    }
}
```

Report findings using your normal review output and severity scale.

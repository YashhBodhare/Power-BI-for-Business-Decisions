# 🟠 Data modelling
[← Study hub](../README.md) · [Shared case](../CASE_STUDY.md) · [Cheat sheet](../CHEAT_SHEET.md)

> [!TIP]
> All applications refer to fictional PayBridge. These are proposed approaches, not claims of real employment or completed project work. Expand the answer after attempting the question.

<a id="pbi-012"></a>
## PBI-012 · Facts and dimensions

**Interview question**

Can you describe the differences between fact tables and dimension tables?

<details>
<summary><strong>💡 Answer + PayBridge business scenario</strong></summary>

### Clear answer

A fact table records events or observations at a declared grain. Dimensions describe entities used for filtering and grouping. Keys link the two; do not combine facts of different grains in one wide table without controlling duplication.

### 🧑‍💼 Same case: PayBridge

**Situation:** Retries and settlement records describe different events.

**My BA approach:** Keep FactAttempt at one row per attempt and FactSettlement at one row per successful payment settlement.

**What I validate:** Reconcile AttemptID and PaymentID uniqueness at their respective grains.

**Decision supported:** Avoid counting retries as extra successful payments.

**Interview-ready response**

> “At fictional PayBridge, I would keep FactAttempt at one row per attempt and FactSettlement at one row per successful payment settlement. I would reconcile AttemptID and PaymentID uniqueness at their respective grains. This would help the team avoid counting retries as extra successful payments.”

</details>

---

<a id="pbi-013"></a>
## PBI-013 · Column or measure?

**Interview question**

When to go with a calculated column or with a calculated measure?

<details>
<summary><strong>💡 Answer + PayBridge business scenario</strong></summary>

### Clear answer

A calculated column produces a row-level value, usually stored and updated with model processing in Import. A measure is evaluated in query filter context and responds to slicers. Use a column for a required grouping attribute and a measure for an aggregate KPI.

### Applied example

```dax
-- Calculated column in FactSettlement; all fixture rows are settled.
IsLate = FactSettlement[SettlementDate] > FactSettlement[DueDate]

-- Measure, responsive to the current report population.
Success Rate = DIVIDE([Successful Attempts], [Attempt Count])
```

Use the schema and relationships in [CASE_STUDY.md](../CASE_STUDY.md). DAX/M examples are reviewed teaching patterns; they were not executed in a Power BI engine here.

### 🧑‍💼 Same case: PayBridge

**Situation:** The report needs a late-settlement category and a dynamic success rate.

**My BA approach:** Use a stable row classification for grouping and a measure for the rate under selected dates and countries.

**What I validate:** Check refresh timing, category rules and rate behaviour when slicers change.

**Decision supported:** Keep row classifications distinct from interactive KPIs.

**Interview-ready response**

> “At fictional PayBridge, I would use a stable row classification for grouping and a measure for the rate under selected dates and countries. I would check refresh timing, category rules and rate behaviour when slicers change. This would help the team keep row classifications distinct from interactive KPIs.”

</details>

---

<a id="pbi-014"></a>
## PBI-014 · Relationship rules

**Interview question**

What rules must be followed in creating a relationship between two tables in Power BI?

<details>
<summary><strong>💡 Answer + PayBridge business scenario</strong></summary>

### Clear answer

Match compatible key types, set the correct cardinality and choose intentional filter direction. A one-side key must be unique; unmatched fact keys need investigation. Active paths must avoid ambiguity. Many-to-many relationships require a justified model rather than pretending every key is unique.

### 🧑‍💼 Same case: PayBridge

**Situation:** An attempt must map to exactly one merchant record.

**My BA approach:** Create a single-direction one-to-many relationship from DimMerchant to FactAttempt.

**What I validate:** Test duplicate dimension keys, orphan fact keys and slicer propagation.

**Decision supported:** Make merchant comparisons trustworthy.

**Interview-ready response**

> “At fictional PayBridge, I would create a single-direction one-to-many relationship from DimMerchant to FactAttempt. I would test duplicate dimension keys, orphan fact keys and slicer propagation. This would help the team make merchant comparisons trustworthy.”

</details>

---

<a id="pbi-015"></a>
## PBI-015 · What is a data model?

**Interview question**

What is a data model in Power BI?

<details>
<summary><strong>💡 Answer + PayBridge business scenario</strong></summary>

### Clear answer

A semantic model combines tables, relationships, measures, metadata and security so reports use consistent definitions. It is more than a set of imported files. Agree grain, calendar, business rules and access before designing visuals.

### 🧑‍💼 Same case: PayBridge

**Situation:** Finance and Operations report different success rates.

**My BA approach:** Define one model with an approved attempt-based numerator and denominator.

**What I validate:** Reconcile both teams' populations and publish a metric dictionary.

**Decision supported:** Provide one shared meaning for the KPI.

**Interview-ready response**

> “At fictional PayBridge, I would define one model with an approved attempt-based numerator and denominator. I would reconcile both teams' populations and publish a metric dictionary. This would help the team provide one shared meaning for the KPI.”

</details>

---

<a id="pbi-016"></a>
## PBI-016 · Column versus measure performance

**Interview question**

Which gives good performance - calculated column or calculated measure?

<details>
<summary><strong>💡 Answer + PayBridge business scenario</strong></summary>

### Clear answer

Neither is universally faster. Columns consume model space and are useful for filtering or grouping; measures compute at query time and may be expensive if poorly written. Compare the actual design, cardinality and workload.

### Applied example

```dax
Fee Revenue INR =
SUMX(
    FILTER(FactAttempt, FactAttempt[Status] = "Succeeded"),
    FactAttempt[AmountINR] * FactAttempt[FeeRate]
)
```

Use the schema and relationships in [CASE_STUDY.md](../CASE_STUDY.md). DAX/M examples are reviewed teaching patterns; they were not executed in a Power BI engine here.

### 🧑‍💼 Same case: PayBridge

**Situation:** A stored amount-derived column increases model size.

**My BA approach:** Evaluate whether the report needs that column or a measure can calculate the required aggregation.

**What I validate:** Compare model size, visual timings and identical results.

**Decision supported:** Choose the simplest design that meets the response-time target.

**Interview-ready response**

> “At fictional PayBridge, I would evaluate whether the report needs that column or a measure can calculate the required aggregation. I would compare model size, visual timings and identical results. This would help the team choose the simplest design that meets the response-time target.”

</details>

---

<a id="pbi-017"></a>
## PBI-017 · Clustered and nonclustered indexes

**Interview question**

What is a clustered index and non-clustered index?

<details>
<summary><strong>💡 Answer + PayBridge business scenario</strong></summary>

### Clear answer

In SQL Server, a clustered index organises the table's rowstore data at its leaf level; a nonclustered index provides a separate access structure. Columnstore has different organisation. These are source-database concepts, not indexes you create on Power BI visual fields.

### 🧑‍💼 Same case: PayBridge

**Situation:** A folded SQL query filtering attempt dates is slow.

**My BA approach:** Work with the database owner to inspect its plan and appropriate source indexes.

**What I validate:** Measure reads and timings before and after while checking unchanged rows.

**Decision supported:** Improve source access without confusing it with semantic-model tuning.

**Interview-ready response**

> “At fictional PayBridge, I would work with the database owner to inspect its plan and appropriate source indexes. I would measure reads and timings before and after while checking unchanged rows. This would help the team improve source access without confusing it with semantic-model tuning.”

</details>

---

<a id="pbi-018"></a>
## PBI-018 · Scalable modelling

**Interview question**

When designing a data model, what factors do you consider to ensure scalability and performance?

<details>
<summary><strong>💡 Answer + PayBridge business scenario</strong></summary>

### Clear answer

Start with a star schema, explicit grain, suitable types and only needed columns. Reduce unnecessary high-cardinality data, plan retention and refresh, and measure report queries. Storage mode and capacity choices must fit freshness and usage requirements.

### 🧑‍💼 Same case: PayBridge

**Situation:** Attempt history grows while morning reports miss their deadline.

**My BA approach:** Agree retention, partition/refresh policy and a fit-for-purpose detail level with stakeholders.

**What I validate:** Check peak concurrency, refresh duration, memory and reconciled KPIs.

**Decision supported:** Scale reporting without unnecessary operational cost.

**Interview-ready response**

> “At fictional PayBridge, I would agree retention, partition/refresh policy and a fit-for-purpose detail level with stakeholders. I would check peak concurrency, refresh duration, memory and reconciled KPIs. This would help the team scale reporting without unnecessary operational cost.”

</details>

---

<a id="pbi-019"></a>
## PBI-019 · Role-playing dimensions and bridges

**Interview question**

Have you implemented any advanced modeling techniques in Power BI, such as role-playing dimensions or bridge tables? If yes, can you provide an example?

<details>
<summary><strong>💡 Answer + PayBridge business scenario</strong></summary>

### Clear answer

A role-playing dimension is used in different roles, such as attempt date and settlement date. Use separate role dimensions or carefully controlled active/inactive relationships. A bridge represents a justified many-to-many mapping; its grain and filter paths must be explicit.

### Applied example

```dax
-- Requires the documented inactive DimDate[Date] -> FactSettlement[DueDate] relationship.
Settled Amount by Due Date =
CALCULATE(
    [Settled Amount INR],
    USERELATIONSHIP(DimDate[Date], FactSettlement[DueDate])
)
```

Use the schema and relationships in [CASE_STUDY.md](../CASE_STUDY.md). DAX/M examples are reviewed teaching patterns; they were not executed in a Power BI engine here.

### 🧑‍💼 Same case: PayBridge

**Situation:** Managers compare payments by attempt date and settlement date.

**My BA approach:** Offer clearly named date roles or a measure that deliberately activates the settlement-date relationship.

**What I validate:** Test the same payment under both date interpretations.

**Decision supported:** Prevent calendar-role confusion in reconciliation.

**Interview-ready response**

> “At fictional PayBridge, I would offer clearly named date roles or a measure that deliberately activates the settlement-date relationship. I would test the same payment under both date interpretations. This would help the team prevent calendar-role confusion in reconciliation.”

</details>

---

<a id="pbi-020"></a>
## PBI-020 · Slowly changing dimensions

**Interview question**

How do you handle slowly changing dimensions (SCDs) in your data model?

<details>
<summary><strong>💡 Answer + PayBridge business scenario</strong></summary>

### Clear answer

SCD Type 1 replaces attributes; Type 2 retains effective-dated versions with surrogate keys. Historical facts should map to the version valid at the business event. This mapping is usually prepared upstream, not inferred from a current merchant record at report time.

### 🧑‍💼 Same case: PayBridge

**Situation:** A merchant changes its risk tier during the year.

**My BA approach:** Define whether historical performance uses event-time or current tier and implement that policy.

**What I validate:** Check transactions around the effective-date boundary.

**Decision supported:** Make historical risk comparisons valid.

**Interview-ready response**

> “At fictional PayBridge, I would define whether historical performance uses event-time or current tier and implement that policy. I would check transactions around the effective-date boundary. This would help the team make historical risk comparisons valid.”

</details>

---

<a id="pbi-021"></a>
## PBI-021 · Calculated tables

**Interview question**

Have you worked with calculated tables in Power BI? Can you explain their purpose and when to use them?

<details>
<summary><strong>💡 Answer + PayBridge business scenario</strong></summary>

### Clear answer

A calculated table is defined with DAX and materialised during model processing, rather than recalculated as a slicer-responsive visual table. It can support helper structures or a calendar, but it adds storage and dependencies. A virtual table inside a measure or query is different.

### Applied example

```dax
-- Calculated table; mark as date table using [Date] for the classic examples.
DimDate =
ADDCOLUMNS(
    CALENDAR(DATE(2024, 1, 1), DATE(2026, 12, 31)),
    "Year", YEAR([Date]),
    "MonthNumber", MONTH([Date]),
    "YearMonth", FORMAT([Date], "yyyy-MM"),
    "YearMonthSort", YEAR([Date]) * 100 + MONTH([Date])
)
```

Use the schema and relationships in [CASE_STUDY.md](../CASE_STUDY.md). DAX/M examples are reviewed teaching patterns; they were not executed in a Power BI engine here.

### 🧑‍💼 Same case: PayBridge

**Situation:** PayBridge needs a complete analysis calendar.

**My BA approach:** Create and configure DimDate with a continuous range covering attempts and settlements.

**What I validate:** Check unique nonblank dates and relationships to both facts.

**Decision supported:** Support reliable date filtering and time comparisons.

**Interview-ready response**

> “At fictional PayBridge, I would create and configure DimDate with a continuous range covering attempts and settlements. I would check unique nonblank dates and relationships to both facts. This would help the team support reliable date filtering and time comparisons.”

</details>

---

<a id="pbi-022"></a>
## PBI-022 · Relationships and hierarchies

**Interview question**

What strategies do you employ for handling complex relationships or hierarchies in your data model?

<details>
<summary><strong>💡 Answer + PayBridge business scenario</strong></summary>

### Clear answer

Use a clear star schema and explicitly defined drill paths. Avoid ambiguous loops and unnecessary bidirectional filtering. A hierarchy controls analytical navigation; it does not replace a relationship or guarantee meaningful additive totals.

### 🧑‍💼 Same case: PayBridge

**Situation:** Users want country-to-city-to-merchant exploration.

**My BA approach:** Define a geographic drill path and the proper dimensions for each level.

**What I validate:** Check merchants are assigned consistently and totals reconcile at each level.

**Decision supported:** Enable detail exploration without contradictory rollups.

**Interview-ready response**

> “At fictional PayBridge, I would define a geographic drill path and the proper dimensions for each level. I would check merchants are assigned consistently and totals reconcile at each level. This would help the team enable detail exploration without contradictory rollups.”

</details>

---

<a id="pbi-023"></a>
## PBI-023 · Large data volumes

**Interview question**

How do you handle large datasets or data volumes in Power BI to ensure smooth performance?

<details>
<summary><strong>💡 Answer + PayBridge business scenario</strong></summary>

### Clear answer

Reduce unnecessary rows and columns, use appropriate storage and aggregation, and plan refresh. Import, DirectQuery, Direct Lake and hybrid patterns have distinct trade-offs. Incremental refresh helps suitable Import history; it is not a universal cure for slow DAX.

### 🧑‍💼 Same case: PayBridge

**Situation:** The report needs two years of attempts but only recent daily updates.

**My BA approach:** Evaluate a supported incremental refresh window and an aggregated executive view.

**What I validate:** Check late updates, query folding, retained history and refreshed partition results.

**Decision supported:** Keep the report timely without repeatedly loading all history.

**Interview-ready response**

> “At fictional PayBridge, I would evaluate a supported incremental refresh window and an aggregated executive view. I would check late updates, query folding, retained history and refreshed partition results. This would help the team keep the report timely without repeatedly loading all history.”

</details>

---

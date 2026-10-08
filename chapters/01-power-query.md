# 🟡 Power Query
[← Study hub](../README.md) · [Shared case](../CASE_STUDY.md) · [Cheat sheet](../CHEAT_SHEET.md)

> [!TIP]
> All applications refer to fictional PayBridge. These are proposed approaches, not claims of real employment or completed project work. Expand the answer after attempting the question.

<a id="pbi-001"></a>
## PBI-001 · Query folding

**Interview question**

What is Query Folding in Power Query and the Power BI Query Editor?

<details>
<summary><strong>💡 Answer + PayBridge business scenario</strong></summary>

### Clear answer

Query folding lets supported Power Query steps run at the source instead of locally. It can be full, partial or absent; connector capabilities and transformations determine what folds. Check folding indicators, query plans or source traces rather than assuming every step folds.

### 🧑‍💼 Same case: PayBridge

**Situation:** A daily payment extract has become slow.

**My BA approach:** Push eligible date filters and column selection to the supported SQL source before expensive local work.

**What I validate:** Compare source queries, transferred rows and unchanged totals.

**Decision supported:** Reduce refresh cost without changing the payment population.

**Interview-ready response**

> “At fictional PayBridge, I would push eligible date filters and column selection to the supported SQL source before expensive local work. I would compare source queries, transferred rows and unchanged totals. This would help the team reduce refresh cost without changing the payment population.”

</details>

---

<a id="pbi-002"></a>
## PBI-002 · The M language

**Interview question**

What is M Language in Power BI?

<details>
<summary><strong>💡 Answer + PayBridge business scenario</strong></summary>

### Clear answer

M is Power Query's expression language for connecting, shaping and combining data. The interface generates M steps that can be inspected in Advanced Editor. M prepares data; DAX defines model calculations, so the two have different jobs.

### Applied example

```powerquery
// Case cleanup only; use the mapping function in question 007 for canonical aliases.
Table.TransformColumns(
    Source,
    {{"Status", each if _ = null then "Unknown" else Text.Proper(Text.Trim(_)), type text}}
)
```

Use the schema and relationships in [CASE_STUDY.md](../CASE_STUDY.md). DAX/M examples are reviewed teaching patterns; they were not executed in a Power BI engine here.

### 🧑‍💼 Same case: PayBridge

**Situation:** Payment statuses arrive with inconsistent casing.

**My BA approach:** Use documented M transformations to standardise the approved status values before loading the model.

**What I validate:** Retain unmapped statuses as exceptions instead of silently calling them failed.

**Decision supported:** Make status-based reporting consistent across sources.

**Interview-ready response**

> “At fictional PayBridge, I would use documented M transformations to standardise the approved status values before loading the model. I would retain unmapped statuses as exceptions instead of silently calling them failed. This would help the team make status-based reporting consistent across sources.”

</details>

---

<a id="pbi-003"></a>
## PBI-003 · Append versus merge

**Interview question**

Difference between the Append and Merge?

<details>
<summary><strong>💡 Answer + PayBridge business scenario</strong></summary>

### Clear answer

Append stacks rows using column names; missing columns produce nulls. Merge matches rows through selected keys and join kind. Duplicate keys can multiply results, so establish table grain and matching rules first.

### Applied example

```powerquery
// Queries with compatible schemas; validate AttemptID uniqueness after append.
Table.Combine({JanuaryAttempts, FebruaryAttempts})
```

Use the schema and relationships in [CASE_STUDY.md](../CASE_STUDY.md). DAX/M examples are reviewed teaching patterns; they were not executed in a Power BI engine here.

### 🧑‍💼 Same case: PayBridge

**Situation:** PayBridge receives monthly attempt files and a merchant master.

**My BA approach:** Append compatible monthly extracts, then enrich attempts with a unique merchant lookup.

**What I validate:** Check duplicate AttemptID values and row counts before and after the merge.

**Decision supported:** Combine months without inflating attempts or losing merchant context.

**Interview-ready response**

> “At fictional PayBridge, I would append compatible monthly extracts, then enrich attempts with a unique merchant lookup. I would check duplicate AttemptID values and row counts before and after the merge. This would help the team combine months without inflating attempts or losing merchant context.”

</details>

---

<a id="pbi-004"></a>
## PBI-004 · Parameters

**Interview question**

What is a Parameter?

<details>
<summary><strong>💡 Answer + PayBridge business scenario</strong></summary>

### Clear answer

A Power Query parameter holds a configurable value such as a file path, server or date boundary. It is not automatically an interactive report slicer. Changing a query parameter generally changes retrieval or transformation and may require refresh.

### 🧑‍💼 Same case: PayBridge

**Situation:** The same solution moves from development to production.

**My BA approach:** Parameterise environment-specific connections and document who may change them.

**What I validate:** Confirm the production parameter points to the approved source and the refresh succeeds.

**Decision supported:** Deploy consistently without hard-coded development paths.

**Interview-ready response**

> “At fictional PayBridge, I would parameterise environment-specific connections and document who may change them. I would confirm the production parameter points to the approved source and the refresh succeeds. This would help the team deploy consistently without hard-coded development paths.”

</details>

---

<a id="pbi-005"></a>
## PBI-005 · How many tables can be combined?

**Interview question**

How many tables can you append & merge?

<details>
<summary><strong>💡 Answer + PayBridge business scenario</strong></summary>

### Clear answer

Append can combine two or multiple tables; merge joins two queries in one operation, and the result can be merged again. There is no useful universal two-table limit for the whole workflow. Practical limits come from schema, volume, resources and source restrictions.

### Applied example

```powerquery
// Queries with compatible schemas; validate AttemptID uniqueness after append.
Table.Combine({JanuaryAttempts, FebruaryAttempts})
```

Use the schema and relationships in [CASE_STUDY.md](../CASE_STUDY.md). DAX/M examples are reviewed teaching patterns; they were not executed in a Power BI engine here.

### 🧑‍💼 Same case: PayBridge

**Situation:** Twelve monthly attempt extracts must become one annual table.

**My BA approach:** Use an append workflow with a standard schema, then perform separately validated reference merges.

**What I validate:** Check every month is included exactly once and duplicate keys are rejected.

**Decision supported:** Build a complete year without accidental duplication.

**Interview-ready response**

> “At fictional PayBridge, I would use an append workflow with a standard schema, then perform separately validated reference merges. I would check every month is included exactly once and duplicate keys are rejected. This would help the team build a complete year without accidental duplication.”

</details>

---

<a id="pbi-006"></a>
## PBI-006 · Power Query versus model storage

**Interview question**

What is the storage engine used in Power Query?

<details>
<summary><strong>💡 Answer + PayBridge business scenario</strong></summary>

### Clear answer

Power Query uses its mashup engine to evaluate M and can delegate work to sources through folding. It is not itself the VertiPaq semantic-model storage engine. Import tables use compressed columnar model storage; other storage modes behave differently.

### 🧑‍💼 Same case: PayBridge

**Situation:** The team confuses transformation time with report query time.

**My BA approach:** Separate source retrieval, M transformation, model loading and visual query timings.

**What I validate:** Locate which stage actually misses the agreed deadline.

**Decision supported:** Optimise the real bottleneck instead of naming the wrong engine.

**Interview-ready response**

> “At fictional PayBridge, I would separate source retrieval, M transformation, model loading and visual query timings. I would locate which stage actually misses the agreed deadline. This would help the team optimise the real bottleneck instead of naming the wrong engine.”

</details>

---

<a id="pbi-007"></a>
## PBI-007 · Custom functions and parameters

**Interview question**

Have you used custom functions or parameters in Power Query? Can you provide an example?

<details>
<summary><strong>💡 Answer + PayBridge business scenario</strong></summary>

### Clear answer

A custom M function packages reusable transformation logic; parameters supply configurable inputs. Use them when repeated rules justify reuse, and check performance because row-by-row functions can restrict folding or add overhead.

### Applied example

```powerquery
// Reusable function; returns an exception category for unrecognised values.
(status as nullable text) as text =>
let
    cleaned = if status = null then "" else Text.Upper(Text.Trim(status)),
    result = if List.Contains({"SUCCESS", "SUCCEEDED"}, cleaned) then "Succeeded"
             else if List.Contains({"FAIL", "FAILED"}, cleaned) then "Failed"
             else if cleaned = "PENDING" then "Pending" else "Unknown"
in
    result
```

Use the schema and relationships in [CASE_STUDY.md](../CASE_STUDY.md). DAX/M examples are reviewed teaching patterns; they were not executed in a Power BI engine here.

### 🧑‍💼 Same case: PayBridge

**Situation:** Each source uses its own spelling for successful payments.

**My BA approach:** Create one approved normalisation function and an explicit source-path parameter.

**What I validate:** Test known aliases, null input and unexpected status text.

**Decision supported:** Apply the same rule in every extract and expose exceptions.

**Interview-ready response**

> “At fictional PayBridge, I would create one approved normalisation function and an explicit source-path parameter. I would test known aliases, null input and unexpected status text. This would help the team apply the same rule in every extract and expose exceptions.”

</details>

---

<a id="pbi-008"></a>
## PBI-008 · Connections and credentials

**Interview question**

How do you handle data source connections and credentials in Power Query?

<details>
<summary><strong>💡 Answer + PayBridge business scenario</strong></summary>

### Clear answer

Manage connection settings and credentials through the appropriate Desktop or service connection settings. Use an authorised identity, privacy levels and gateway where required. Do not embed passwords in M or assume Desktop credentials automatically work in the service.

### 🧑‍💼 Same case: PayBridge

**Situation:** A report refresh fails after publication.

**My BA approach:** Check the service connection identity, permissions and gateway mapping with the platform owner.

**What I validate:** Perform a service-side refresh and verify only authorised data is accessible.

**Decision supported:** Restore reliable refresh with accountable access.

**Interview-ready response**

> “At fictional PayBridge, I would check the service connection identity, permissions and gateway mapping with the platform owner. I would perform a service-side refresh and verify only authorised data is accessible. This would help the team restore reliable refresh with accountable access.”

</details>

---

<a id="pbi-009"></a>
## PBI-009 · Custom and conditional columns

**Interview question**

Have you worked with custom column transformations or conditional logic in Power Query? Can you provide an example?

<details>
<summary><strong>💡 Answer + PayBridge business scenario</strong></summary>

### Clear answer

Power Query custom columns use M expressions; conditional columns encode branching rules. Define null handling and priority when conditions overlap. Prefer upstream transformations for stable row-level preparation where appropriate.

### Applied example

```powerquery
// Case cleanup only; use the mapping function in question 007 for canonical aliases.
Table.TransformColumns(
    Source,
    {{"Status", each if _ = null then "Unknown" else Text.Proper(Text.Trim(_)), type text}}
)
```

Use the schema and relationships in [CASE_STUDY.md](../CASE_STUDY.md). DAX/M examples are reviewed teaching patterns; they were not executed in a Power BI engine here.

### 🧑‍💼 Same case: PayBridge

**Situation:** Operations needs attempts grouped into approved status categories.

**My BA approach:** Add a normalised status column that distinguishes Succeeded, Failed, Pending and Unknown.

**What I validate:** Check unmatched values and never turn a missing status into success.

**Decision supported:** Make failure analysis explainable and auditable.

**Interview-ready response**

> “At fictional PayBridge, I would add a normalised status column that distinguishes Succeeded, Failed, Pending and Unknown. I would check unmatched values and never turn a missing status into success. This would help the team make failure analysis explainable and auditable.”

</details>

---

<a id="pbi-010"></a>
## PBI-010 · Types and data quality

**Interview question**

What techniques do you use to handle data type conversions and data quality checks in Power Query?

<details>
<summary><strong>💡 Answer + PayBridge business scenario</strong></summary>

### Clear answer

Set explicit data types and locale-aware conversions; inspect conversion errors, nulls, duplicates and profiling scope. A successful type cast does not prove business validity. Preserve rejected records and reconcile counts.

### Applied example

```powerquery
Table.TransformColumnTypes(
    Source,
    {{"AttemptID", type text}, {"AttemptDate", type date}, {"AmountINR", Currency.Type}},
    "en-US"
)
```

Use the schema and relationships in [CASE_STUDY.md](../CASE_STUDY.md). DAX/M examples are reviewed teaching patterns; they were not executed in a Power BI engine here.

### 🧑‍💼 Same case: PayBridge

**Situation:** Attempt dates and INR amounts arrive as text.

**My BA approach:** Convert with the correct source locale, validate keys and quarantine invalid records.

**What I validate:** Test ambiguous dates, malformed amounts, missing IDs and duplicate attempts.

**Decision supported:** Prevent bad source values from distorting the payment KPIs.

**Interview-ready response**

> “At fictional PayBridge, I would convert with the correct source locale, validate keys and quarantine invalid records. I would test ambiguous dates, malformed amounts, missing IDs and duplicate attempts. This would help the team prevent bad source values from distorting the payment KPIs.”

</details>

---

<a id="pbi-011"></a>
## PBI-011 · CALCULATETABLE versus FILTER

**Interview question**

Difference between calculate table & filter?

<details>
<summary><strong>💡 Answer + PayBridge business scenario</strong></summary>

### Clear answer

These are DAX functions, not Power Query functions. CALCULATETABLE evaluates a table expression in a modified filter context; FILTER iterates a table and returns rows satisfying a predicate. They can be combined but are not interchangeable.

### Applied example

```dax
-- Virtual table in a DAX query; not a slicer-responsive stored calculated table.
EVALUATE
CALCULATETABLE(FactAttempt, KEEPFILTERS(FactAttempt[Status] = "Failed"))
```

Use the schema and relationships in [CASE_STUDY.md](../CASE_STUDY.md). DAX/M examples are reviewed teaching patterns; they were not executed in a Power BI engine here.

### 🧑‍💼 Same case: PayBridge

**Situation:** An analyst needs a virtual table of failed attempts for investigation.

**My BA approach:** Choose a context-based filter for a simple status rule or FILTER for a genuinely row-dependent condition.

**What I validate:** Check the selected rows against the approved definition and current report filters.

**Decision supported:** Return the intended exception population.

**Interview-ready response**

> “At fictional PayBridge, I would choose a context-based filter for a simple status rule or FILTER for a genuinely row-dependent condition. I would check the selected rows against the approved definition and current report filters. This would help the team return the intended exception population.”

</details>

---

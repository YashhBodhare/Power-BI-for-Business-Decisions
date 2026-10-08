# 🔵 Service and connectivity
[← Study hub](../README.md) · [Shared case](../CASE_STUDY.md) · [Cheat sheet](../CHEAT_SHEET.md)

> [!TIP]
> All applications refer to fictional PayBridge. These are proposed approaches, not claims of real employment or completed project work. Expand the answer after attempting the question.

<a id="pbi-037"></a>
## PBI-037 · The Power BI service

**Interview question**

What is Power BI service?

<details>
<summary><strong>💡 Answer + PayBridge business scenario</strong></summary>

### Clear answer

The service supports hosting, collaboration, access control, distribution and managed refresh of Power BI content. Desktop is primarily an authoring tool. Publication does not itself configure every connection, security role or refresh setting.

### 🧑‍💼 Same case: PayBridge

**Situation:** PayBridge must share an approved payments report.

**My BA approach:** Publish through governed workspaces, validate service connections and distribute the approved app.

**What I validate:** Check access, refresh history and representative user behaviour.

**Decision supported:** Provide a controlled shared reporting experience.

**Interview-ready response**

> “At fictional PayBridge, I would publish through governed workspaces, validate service connections and distribute the approved app. I would check access, refresh history and representative user behaviour. This would help the team provide a controlled shared reporting experience.”

</details>

---

<a id="pbi-038"></a>
## PBI-038 · Licensing choices

**Interview question**

What licenses are available in Power BI?

<details>
<summary><strong>💡 Answer + PayBridge business scenario</strong></summary>

### Clear answer

Distinguish Free, Pro and Premium Per User licences from capacity licensing such as Fabric F capacity. Authoring, sharing and viewing requirements depend on workspace and capacity. For eligible F64+ capacity, Free viewers can consume appropriately shared content; PPU content generally requires PPU. Check current terms rather than quoting old prices.

### 🧑‍💼 Same case: PayBridge

**Situation:** A small authoring team serves a larger audience.

**My BA approach:** Map authors, consumers and required features before comparing licence and capacity options.

**What I validate:** Confirm actual workspace configuration and viewer entitlements.

**Decision supported:** Choose a supported distribution plan.

**Interview-ready response**

> “At fictional PayBridge, I would map authors, consumers and required features before comparing licence and capacity options. I would confirm actual workspace configuration and viewer entitlements. This would help the team choose a supported distribution plan.”

</details>

---

<a id="pbi-039"></a>
## PBI-039 · Your actual licence

**Interview question**

Which license do you have?

<details>
<summary><strong>💡 Answer + PayBridge business scenario</strong></summary>

### Clear answer

Answer from your real account and environment. Do not invent a Pro or PPU subscription. Explain what that licence enabled and how production deployment could differ. The case study does not establish your personal licence.

### 🧑‍💼 Same case: PayBridge

**Situation:** An interviewer asks which licence you used.

**My BA approach:** State the verified licence or say you need to confirm it, then separate learning from deployment requirements.

**What I validate:** Check account details before making a factual experience claim.

**Decision supported:** Demonstrate honest understanding of the environment.

**Interview-ready response**

> “At fictional PayBridge, I would state the verified licence or say you need to confirm it, then separate learning from deployment requirements. I would check account details before making a factual experience claim. This would help the team demonstrate honest understanding of the environment.”

</details>

---

<a id="pbi-040"></a>
## PBI-040 · Embedding

**Interview question**

Are there options available for embedding Power BI into other applications or portals?

<details>
<summary><strong>💡 Answer + PayBridge business scenario</strong></summary>

### Clear answer

Embedding for an organisation and embedding for external customers have different identity and licensing patterns. Use an authenticated design with applicable capacity, effective identity and RLS. Publish to web is public access and is unsuitable for sensitive payment data.

### 🧑‍💼 Same case: PayBridge

**Situation:** Merchants want payment analytics in an authenticated portal.

**My BA approach:** Define tenant isolation and an approved embedded architecture with the security team.

**What I validate:** Test one merchant cannot access another merchant's records.

**Decision supported:** Provide convenient access without exposing payment information.

**Interview-ready response**

> “At fictional PayBridge, I would define tenant isolation and an approved embedded architecture with the security team. I would test one merchant cannot access another merchant's records. This would help the team provide convenient access without exposing payment information.”

</details>

---

<a id="pbi-041"></a>
## PBI-041 · Row-level security

**Interview question**

What is RLS (Row Level Security)?

<details>
<summary><strong>💡 Answer + PayBridge business scenario</strong></summary>

### Clear answer

RLS filters rows for authorised identities through model roles and security relationships. In the service it applies to consumers such as Viewers, not workspace Admins, Members or Contributors with editing access. Test the actual roles and app experience; slicers are not RLS.

### Applied example

```dax
-- RLS rule on DimCountry; UserCountryAccess is a disconnected entitlement table.
-- Create one consumer role; also add the DimMerchant and UserCountryAccess
-- rules documented in CASE_STUDY.md, then test actual Viewer access.
DimCountry[CountryKey] IN
SELECTCOLUMNS(
    FILTER(UserCountryAccess, UserCountryAccess[UPN] = USERPRINCIPALNAME()),
    "AllowedCountryKey", UserCountryAccess[CountryKey]
)
```

Use the schema and relationships in [CASE_STUDY.md](../CASE_STUDY.md). DAX/M examples are reviewed teaching patterns; they were not executed in a Power BI engine here.

### 🧑‍💼 Same case: PayBridge

**Situation:** Regional operations users should see only assigned countries.

**My BA approach:** Maintain a user-to-country entitlement table and a security path to the facts.

**What I validate:** Test allowed, denied, unmapped and multi-country users using consumer access.

**Decision supported:** Enforce the agreed row visibility.

**Interview-ready response**

> “At fictional PayBridge, I would maintain a user-to-country entitlement table and a security path to the facts. I would test allowed, denied, unmapped and multi-country users using consumer access. This would help the team enforce the agreed row visibility.”

</details>

---

<a id="pbi-042"></a>
## PBI-042 · Gateways

**Interview question**

What is a gateway? How many types? How does it work?

<details>
<summary><strong>💡 Answer + PayBridge business scenario</strong></summary>

### Clear answer

A gateway provides supported connectivity from the service to data behind a network boundary. The standard on-premises gateway supports shared managed use; personal mode serves a narrower individual scenario. A virtual-network gateway is a separate managed option where supported. The required choice depends on source, network and features.

### 🧑‍💼 Same case: PayBridge

**Situation:** The warehouse is reachable on an internal network but service refresh fails.

**My BA approach:** Coordinate a supported gateway and connection mapping with the platform owner.

**What I validate:** Check gateway availability, credentials, permissions and refresh results.

**Decision supported:** Maintain dependable service access to the approved source.

**Interview-ready response**

> “At fictional PayBridge, I would coordinate a supported gateway and connection mapping with the platform owner. I would check gateway availability, credentials, permissions and refresh results. This would help the team maintain dependable service access to the approved source.”

</details>

---

<a id="pbi-043"></a>
## PBI-043 · Alerts

**Interview question**

How can you set the alerts in Power BI service?

<details>
<summary><strong>💡 Answer + PayBridge business scenario</strong></summary>

### Clear answer

Classic service data alerts apply to supported numeric dashboard tiles such as cards, KPIs and gauges, subject to their limitations. They evaluate updated data, not every transaction in real time. Newer Fabric alerting options have different requirements; choose from the actual workspace capabilities.

### 🧑‍💼 Same case: PayBridge

**Situation:** Operations needs notice when the failure rate exceeds an agreed threshold.

**My BA approach:** Configure a supported monitored KPI, refresh expectations and an actionable notification owner.

**What I validate:** Test the threshold, evaluation timing and duplicate-notification behaviour.

**Decision supported:** Turn monitoring into accountable follow-up.

**Interview-ready response**

> “At fictional PayBridge, I would configure a supported monitored KPI, refresh expectations and an actionable notification owner. I would test the threshold, evaluation timing and duplicate-notification behaviour. This would help the team turn monitoring into accountable follow-up.”

</details>

---

<a id="pbi-044"></a>
## PBI-044 · Microsoft Fabric

**Interview question**

What is Microsoft fabric?

<details>
<summary><strong>💡 Answer + PayBridge business scenario</strong></summary>

### Clear answer

Fabric is Microsoft's analytics platform bringing data engineering, warehousing, real-time analytics and Power BI workloads together with OneLake. It is not simply a renamed dashboard. Capacity, governance and access still need design.

### 🧑‍💼 Same case: PayBridge

**Situation:** PayBridge wants one governed route from payment sources to reporting.

**My BA approach:** Evaluate pipelines, warehouse/lakehouse and semantic-model responsibilities against the existing architecture.

**What I validate:** Check ownership, lineage, access and operational cost before adoption.

**Decision supported:** Integrate analytics only where it supports a real requirement.

**Interview-ready response**

> “At fictional PayBridge, I would evaluate pipelines, warehouse/lakehouse and semantic-model responsibilities against the existing architecture. I would check ownership, lineage, access and operational cost before adoption. This would help the team integrate analytics only where it supports a real requirement.”

</details>

---

<a id="pbi-045"></a>
## PBI-045 · Source-to-visual validation

**Interview question**

How will you test from the source side once the visual is built in Power BI Desktop?

<details>
<summary><strong>💡 Answer + PayBridge business scenario</strong></summary>

### Clear answer

Reconcile the visual with an independent source query using the same grain, period, statuses and security scope. Check transformations, relationships and measure filters, not just a single grand total. Trace representative records and document exclusions.

### 🧑‍💼 Same case: PayBridge

**Situation:** A visual shows a higher successful amount than Finance expects.

**My BA approach:** Compare source and model totals by date and merchant, then trace unmatched or duplicated payment IDs.

**What I validate:** Confirm retries are not double-counted and both sides use the same cut-off.

**Decision supported:** Resolve discrepancies before the report supports decisions.

**Interview-ready response**

> “At fictional PayBridge, I would compare source and model totals by date and merchant, then trace unmatched or duplicated payment IDs. I would confirm retries are not double-counted and both sides use the same cut-off. This would help the team resolve discrepancies before the report supports decisions.”

</details>

---

<a id="pbi-046"></a>
## PBI-046 · Data sources

**Interview question**

What data sources can I connect to Power BI?

<details>
<summary><strong>💡 Answer + PayBridge business scenario</strong></summary>

### Clear answer

Power BI offers connectors for databases, files, cloud platforms and services. Connector support, authentication, folding and storage modes differ. Choose an approved source of truth and verify the connector's actual capabilities.

### 🧑‍💼 Same case: PayBridge

**Situation:** Attempt data lives in SQL Server and merchant reference data comes from an approved export.

**My BA approach:** Use governed connections and document each source's owner and update cadence.

**What I validate:** Check keys, schema changes and freshness across both sources.

**Decision supported:** Build a traceable reporting pipeline.

**Interview-ready response**

> “At fictional PayBridge, I would use governed connections and document each source's owner and update cadence. I would check keys, schema changes and freshness across both sources. This would help the team build a traceable reporting pipeline.”

</details>

---

<a id="pbi-047"></a>
## PBI-047 · Import versus DirectQuery

**Interview question**

Difference between import & direct query mode?

<details>
<summary><strong>💡 Answer + PayBridge business scenario</strong></summary>

### Clear answer

Import stores model data and usually offers fast interactive queries but needs refresh. DirectQuery sends supported queries to the source and depends on its latency, workload and caching. It does not guarantee instant freshness or superior security; compare requirements and measured behaviour.

### 🧑‍💼 Same case: PayBridge

**Situation:** Managers require a daily report, not transaction-by-transaction monitoring.

**My BA approach:** Pilot Import with a refresh SLA against DirectQuery using representative queries.

**What I validate:** Measure visual response, source load and permitted staleness.

**Decision supported:** Choose a mode that meets the business need.

**Interview-ready response**

> “At fictional PayBridge, I would pilot Import with a refresh SLA against DirectQuery using representative queries. I would measure visual response, source load and permitted staleness. This would help the team choose a mode that meets the business need.”

</details>

---

<a id="pbi-048"></a>
## PBI-048 · Connectivity and storage modes

**Interview question**

Types of connectivity modes available in Power BI?

<details>
<summary><strong>💡 Answer + PayBridge business scenario</strong></summary>

### Clear answer

Import and DirectQuery are table storage modes; composite models can mix supported modes, including Dual in suitable designs. Direct Lake is a Fabric option. A live connection reuses an existing semantic model or Analysis Services model, rather than being the same thing as a local imported table.

### 🧑‍💼 Same case: PayBridge

**Situation:** Several reports must reuse approved payment measures.

**My BA approach:** Consider a live connection to the governed model instead of duplicating data and definitions.

**What I validate:** Check feature support, permissions and freshness responsibility.

**Decision supported:** Reuse trusted definitions with an appropriate architecture.

**Interview-ready response**

> “At fictional PayBridge, I would consider a live connection to the governed model instead of duplicating data and definitions. I would check feature support, permissions and freshness responsibility. This would help the team reuse trusted definitions with an appropriate architecture.”

</details>

---

<a id="pbi-049"></a>
## PBI-049 · Sources you actually used

**Interview question**

What are the sources you have used?

<details>
<summary><strong>💡 Answer + PayBridge business scenario</strong></summary>

### Clear answer

Name only sources you genuinely used and explain your contribution. For a hypothetical answer, say what you would use. Access to a connector is not evidence of production experience.

### 🧑‍💼 Same case: PayBridge

**Situation:** An interviewer asks where your payment report data came from.

**My BA approach:** Distinguish the fictional SQL warehouse and JSON learning fixture from your actual project sources.

**What I validate:** Ensure the stated experience matches your work.

**Decision supported:** Build credibility through precise evidence.

**Interview-ready response**

> “At fictional PayBridge, I would distinguish the fictional SQL warehouse and JSON learning fixture from your actual project sources. I would ensure the stated experience matches your work. This would help the team build credibility through precise evidence.”

</details>

---

<a id="pbi-050"></a>
## PBI-050 · Which database?

**Interview question**

From which database will you get the data?

<details>
<summary><strong>💡 Answer + PayBridge business scenario</strong></summary>

### Clear answer

Use the governed analytical source agreed with data owners; the database choice depends on the architecture. Do not assume Power BI requires one specific database or that reporting should query a transactional system directly.

### 🧑‍💼 Same case: PayBridge

**Situation:** PayBridge's payment application has an operational store and an analytical warehouse.

**My BA approach:** Prefer an approved warehouse view with documented grain and freshness for routine BI reporting.

**What I validate:** Check lineage back to operations and reconciliation controls.

**Decision supported:** Protect operational workloads while keeping reports trustworthy.

**Interview-ready response**

> “At fictional PayBridge, I would prefer an approved warehouse view with documented grain and freshness for routine BI reporting. I would check lineage back to operations and reconciliation controls. This would help the team protect operational workloads while keeping reports trustworthy.”

</details>

---

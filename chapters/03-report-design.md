# 🟣 Report design
[← Study hub](../README.md) · [Shared case](../CASE_STUDY.md) · [Cheat sheet](../CHEAT_SHEET.md)

> [!TIP]
> All applications refer to fictional PayBridge. These are proposed approaches, not claims of real employment or completed project work. Expand the answer after attempting the question.

<a id="pbi-024"></a>
## PBI-024 · Report filters

**Interview question**

What are filters in Power BI?

<details>
<summary><strong>💡 Answer + PayBridge business scenario</strong></summary>

### Clear answer

Filters restrict the analysis population at visual, page or report scope; slicers are visible interactive controls. Drillthrough and interactions add other context. A filter is not a security boundary, so access rules belong in security configuration.

### 🧑‍💼 Same case: PayBridge

**Situation:** Operations reviews February failures for one country.

**My BA approach:** Apply a date scope and country selection while making the failed-attempt definition explicit.

**What I validate:** Check what each filter affects and display the scope clearly.

**Decision supported:** Help users interpret the right population.

**Interview-ready response**

> “At fictional PayBridge, I would apply a date scope and country selection while making the failed-attempt definition explicit. I would check what each filter affects and display the scope clearly. This would help the team help users interpret the right population.”

</details>

---

<a id="pbi-025"></a>
## PBI-025 · Model, report and dashboard

**Interview question**

What are the differences between a Power BI Dataset, a Report, and a Dashboard?

<details>
<summary><strong>💡 Answer + PayBridge business scenario</strong></summary>

### Clear answer

Dataset is the older term for semantic model. A report is an interactive set of pages based on a model; a service dashboard is a single canvas of tiles that can draw from different reports. Their capabilities and refresh behaviour differ.

### 🧑‍💼 Same case: PayBridge

**Situation:** Executives need a headline view while analysts need investigation pages.

**My BA approach:** Use a shared model, an investigative report and a service dashboard only if tile-based monitoring is needed.

**What I validate:** Check KPI definitions and freshness agree across presentations.

**Decision supported:** Serve different users without duplicating business logic.

**Interview-ready response**

> “At fictional PayBridge, I would use a shared model, an investigative report and a service dashboard only if tile-based monitoring is needed. I would check KPI definitions and freshness agree across presentations. This would help the team serve different users without duplicating business logic.”

</details>

---

<a id="pbi-026"></a>
## PBI-026 · Cross filtering

**Interview question**

What is cross filtering?

<details>
<summary><strong>💡 Answer + PayBridge business scenario</strong></summary>

### Clear answer

Selecting a data point can filter or highlight other visuals, depending on visual capability and interaction settings. Model relationship filter propagation is a related but distinct concept. Explain which meaning is intended.

### 🧑‍💼 Same case: PayBridge

**Situation:** Selecting a payment channel should narrow the failure details.

**My BA approach:** Configure the interaction to filter the exception table and choose which comparisons remain unchanged.

**What I validate:** Test channel selections, clear selections and affected totals.

**Decision supported:** Make exploratory behaviour predictable.

**Interview-ready response**

> “At fictional PayBridge, I would configure the interaction to filter the exception table and choose which comparisons remain unchanged. I would test channel selections, clear selections and affected totals. This would help the team make exploratory behaviour predictable.”

</details>

---

<a id="pbi-027"></a>
## PBI-027 · Report versus dashboard

**Interview question**

Difference between report & dashboard?

<details>
<summary><strong>💡 Answer + PayBridge business scenario</strong></summary>

### Clear answer

Reports offer multiple pages and rich interactive exploration. Service dashboards provide a one-page tile view and can combine pinned content. A report page is not automatically a dashboard, and dashboard tiles do not offer all report interactions.

### 🧑‍💼 Same case: PayBridge

**Situation:** The CEO wants quick monitoring; Operations needs drillthrough.

**My BA approach:** Choose a dashboard for selected headline tiles and a report for detailed analysis.

**What I validate:** Verify navigation leads users to the correct filtered detail.

**Decision supported:** Match the delivery format to the decision.

**Interview-ready response**

> “At fictional PayBridge, I would choose a dashboard for selected headline tiles and a report for detailed analysis. I would verify navigation leads users to the correct filtered detail. This would help the team match the delivery format to the decision.”

</details>

---

<a id="pbi-028"></a>
## PBI-028 · Dynamic reports

**Interview question**

How do you make a report dynamic?

<details>
<summary><strong>💡 Answer + PayBridge business scenario</strong></summary>

### Clear answer

Use measures, slicers, field parameters, drillthrough and conditional presentation where they support decisions. A measure reacts to filter context; changing visuals does not automatically fetch newer Import data. Distinguish interaction from data freshness.

### Applied example

```dax
-- Dynamic title; does not change Import data freshness.
Country Scope Title =
"Payment performance: " & SELECTEDVALUE(DimCountry[Country], "multiple/all countries")
```

Use the schema and relationships in [CASE_STUDY.md](../CASE_STUDY.md). DAX/M examples are reviewed teaching patterns; they were not executed in a Power BI engine here.

### 🧑‍💼 Same case: PayBridge

**Situation:** A manager switches between failure count and failure rate by channel.

**My BA approach:** Provide an approved metric selector and units-aware titles.

**What I validate:** Test each selection and ensure labels, formatting and denominators stay correct.

**Decision supported:** Offer flexible analysis without misleading comparisons.

**Interview-ready response**

> “At fictional PayBridge, I would provide an approved metric selector and units-aware titles. I would test each selection and ensure labels, formatting and denominators stay correct. This would help the team offer flexible analysis without misleading comparisons.”

</details>

---

<a id="pbi-029"></a>
## PBI-029 · Custom visuals

**Interview question**

Have you implemented any custom visuals or extensions in Power BI? If yes, can you provide an example?

<details>
<summary><strong>💡 Answer + PayBridge business scenario</strong></summary>

### Clear answer

Use a custom visual only for an unmet analytical need and review certification, governance, accessibility, export behaviour and performance. Built-in visuals are often sufficient. Do not claim prior implementation if the case is only a proposal.

### 🧑‍💼 Same case: PayBridge

**Situation:** The team requests a bespoke settlement-flow visual.

**My BA approach:** Evaluate approved options against a simpler built-in alternative and prototype with fictional data.

**What I validate:** Check usability, tenant policy and correct totals.

**Decision supported:** Choose a visual that improves decisions rather than decoration.

**Interview-ready response**

> “At fictional PayBridge, I would evaluate approved options against a simpler built-in alternative and prototype with fictional data. I would check usability, tenant policy and correct totals. This would help the team choose a visual that improves decisions rather than decoration.”

</details>

---

<a id="pbi-030"></a>
## PBI-030 · Filters used in a project

**Interview question**

What kind of filters have you applied in your project?

<details>
<summary><strong>💡 Answer + PayBridge business scenario</strong></summary>

### Clear answer

Describe filters you actually used, their scope and their business purpose. In a hypothetical case, state what you would configure. Examples include date, country, merchant and investigation status; their interactions must be explicit.

### 🧑‍💼 Same case: PayBridge

**Situation:** Finance needs settled payments for one month while Operations tracks attempts.

**My BA approach:** Give each page an appropriate scope and show the selected period.

**What I validate:** Compare counts with source queries under matching rules.

**Decision supported:** Avoid using a settlement population for an attempt-based KPI.

**Interview-ready response**

> “At fictional PayBridge, I would give each page an appropriate scope and show the selected period. I would compare counts with source queries under matching rules. This would help the team avoid using a settlement population for an attempt-based KPI.”

</details>

---

<a id="pbi-031"></a>
## PBI-031 · Bookmarks

**Interview question**

Have you worked with Bookmarks?

<details>
<summary><strong>💡 Answer + PayBridge business scenario</strong></summary>

### Clear answer

Bookmarks can store page, display and data state according to their options. Use selected visuals and disable data capture when a presentation toggle should preserve slicers. Test restoration rather than assuming all saved states are suitable.

### 🧑‍💼 Same case: PayBridge

**Situation:** A page switches between a summary panel and a failure-detail panel.

**My BA approach:** Use a display bookmark that preserves the user's date and country selections.

**What I validate:** Toggle repeatedly and confirm filters do not unexpectedly reset.

**Decision supported:** Support guided exploration without losing context.

**Interview-ready response**

> “At fictional PayBridge, I would use a display bookmark that preserves the user's date and country selections. I would toggle repeatedly and confirm filters do not unexpectedly reset. This would help the team support guided exploration without losing context.”

</details>

---

<a id="pbi-032"></a>
## PBI-032 · Conditional formatting

**Interview question**

Have you used conditional formatting?

<details>
<summary><strong>💡 Answer + PayBridge business scenario</strong></summary>

### Clear answer

Conditional formatting uses values or rules to alter colours, icons or presentation. Define thresholds and direction with the business. Colour should not be the only indicator, and a rate based on very few attempts may need a minimum-volume rule.

### Applied example

```dax
Failure Review Flag =
VAR MinimumAttempts = 100
VAR FailureThreshold = 0.05
RETURN
    IF(
        [Attempt Count] < MinimumAttempts,
        "Insufficient volume",
        IF([Failure Rate] > FailureThreshold, "Investigate", "Within threshold")
    )
-- Illustrative policy only; both thresholds require stakeholder approval.
```

Use the schema and relationships in [CASE_STUDY.md](../CASE_STUDY.md). DAX/M examples are reviewed teaching patterns; they were not executed in a Power BI engine here.

### 🧑‍💼 Same case: PayBridge

**Situation:** A channel's failure rate crosses an agreed investigation threshold.

**My BA approach:** Highlight the rate with an icon and label, including a minimum attempt count.

**What I validate:** Check threshold boundaries, blank rates and low-volume channels.

**Decision supported:** Prioritise investigation without overstating small-sample noise.

**Interview-ready response**

> “At fictional PayBridge, I would highlight the rate with an icon and label, including a minimum attempt count. I would check threshold boundaries, blank rates and low-volume channels. This would help the team prioritise investigation without overstating small-sample noise.”

</details>

---

<a id="pbi-033"></a>
## PBI-033 · Edit interactions: scope

**Interview question**

What does Edit Interactions do at a high level in Power BI Desktop?

<details>
<summary><strong>💡 Answer + PayBridge business scenario</strong></summary>

### Clear answer

Edit interactions controls whether one visual filters, highlights or does not affect another where supported. It changes report behaviour, not RLS or data access. Document the intended scope and test it.

### 🧑‍💼 Same case: PayBridge

**Situation:** A country slicer should affect operational visuals but preserve a global benchmark.

**My BA approach:** Disable its interaction with the benchmark and label that card as global.

**What I validate:** Check selected-country values change while the benchmark remains stable.

**Decision supported:** Keep local and overall comparisons interpretable.

**Interview-ready response**

> “At fictional PayBridge, I would disable its interaction with the benchmark and label that card as global. I would check selected-country values change while the benchmark remains stable. This would help the team keep local and overall comparisons interpretable.”

</details>

---

<a id="pbi-034"></a>
## PBI-034 · Edit interactions: visual behaviour

**Interview question**

What is Edit Interaction in visuals?

<details>
<summary><strong>💡 Answer + PayBridge business scenario</strong></summary>

### Clear answer

Select the controlling visual, open interaction editing and choose the target behaviour for each visual. Capabilities vary by visual. Disabled interactions do not remove other page, report or measure filters.

### 🧑‍💼 Same case: PayBridge

**Situation:** Clicking a bank should filter a failure table but not distort the date trend comparison.

**My BA approach:** Set interactions explicitly and explain the remaining filter context.

**What I validate:** Test clicks, highlighting and reset under existing slicers.

**Decision supported:** Avoid unexpected navigation effects.

**Interview-ready response**

> “At fictional PayBridge, I would set interactions explicitly and explain the remaining filter context. I would test clicks, highlighting and reset under existing slicers. This would help the team avoid unexpected navigation effects.”

</details>

---

<a id="pbi-035"></a>
## PBI-035 · Column versus measure in a report

**Interview question**

Difference between calculated column and measure?

<details>
<summary><strong>💡 Answer + PayBridge business scenario</strong></summary>

### Clear answer

A column supplies row attributes for axes, categories or slicers; a measure calculates an aggregate in current context. A column is not a substitute for a dynamic rate. Decide whether the value describes a row or answers a contextual business question.

### Applied example

```dax
-- Calculated column in FactSettlement; all fixture rows are settled.
IsLate = FactSettlement[SettlementDate] > FactSettlement[DueDate]

-- Measure, responsive to the current report population.
Success Rate = DIVIDE([Successful Attempts], [Attempt Count])
```

Use the schema and relationships in [CASE_STUDY.md](../CASE_STUDY.md). DAX/M examples are reviewed teaching patterns; they were not executed in a Power BI engine here.

### 🧑‍💼 Same case: PayBridge

**Situation:** The page groups settlements by late/on-time status and displays a late rate.

**My BA approach:** Use the late flag as a grouping field and a measure for the selected-population rate.

**What I validate:** Check the denominator and rate when merchants are selected.

**Decision supported:** Combine stable grouping with correct interactive totals.

**Interview-ready response**

> “At fictional PayBridge, I would use the late flag as a grouping field and a measure for the selected-population rate. I would check the denominator and rate when merchants are selected. This would help the team combine stable grouping with correct interactive totals.”

</details>

---

<a id="pbi-036"></a>
## PBI-036 · Filter pane or slicer?

**Interview question**

When do you go for filter & slicer?

<details>
<summary><strong>💡 Answer + PayBridge business scenario</strong></summary>

### Clear answer

Use slicers for visible user choices; use filter-pane settings for scoped constraints or less prominent options. Both contribute filter context. Neither is a substitute for RLS, and hiding a filter is not data protection.

### 🧑‍💼 Same case: PayBridge

**Situation:** Users need to choose a month, while an exception page always focuses on failed attempts.

**My BA approach:** Expose the date slicer and clearly document the page's fixed failure scope.

**What I validate:** Check users can see the page's scope and cannot mistake it for all attempts.

**Decision supported:** Balance usability with consistent report purpose.

**Interview-ready response**

> “At fictional PayBridge, I would expose the date slicer and clearly document the page's fixed failure scope. I would check users can see the page's scope and cannot mistake it for all attempts. This would help the team balance usability with consistent report purpose.”

</details>

---

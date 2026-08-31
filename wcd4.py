import streamlit as st
import pandas as pd
import plotly.express as px

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="Centum Working Capital Command Center",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Centum Working Capital Command Center")
st.markdown(
"""
### Forecast • Benchmark • Optimize • Create Value
"""
)

# ==========================================
# INPUT DATA
# ==========================================

forecast_revenue = 8965.84
forecast_dso = 122.13
forecast_dio = 248.18
forecast_dpo = 135.86

forecast_ccc = (
    forecast_dso +
    forecast_dio -
    forecast_dpo
)

benchmark_ccc = 142.81
benchmark_dso = 86.86
benchmark_dio = 175.62
benchmark_dpo = 119.67

gap_ccc = forecast_ccc - benchmark_ccc

# ==========================================
# WORKING CAPITAL DRIVERS
# ==========================================

forecast_receivables = (
    forecast_revenue *
    forecast_dso /
    360
)

forecast_inventory = (
    forecast_revenue *
    forecast_dio /
    360
)

forecast_payables = (
    forecast_revenue *
    forecast_dpo /
    360
)

working_capital_requirement = (
    forecast_receivables +
    forecast_inventory -
    forecast_payables
)
# ==========================================
# BENCHMARK DATA
# ==========================================

benchmark_df = pd.DataFrame({
    "Company": [
        "Kaynes Technologies",
        "Centum",
        "Astra",
        "Apollo Micro Systems",
        "Datapatterns"
    ],
    "Avg CCC": [
        149.54,
        252.72,
        422.08,
        489.20,
        868.91
    ]
})
# ==========================================
# SIDEBAR
# ==========================================

st.sidebar.header("Scenario Inputs")

interest_rate = st.sidebar.slider(
    "Interest Rate (%)",
    1.0,
    20.0,
    8.0
)

dio_reduction = st.sidebar.slider(
    "Reduce DIO By (Days)",
    0,
    60,
    10
)

dso_reduction = st.sidebar.slider(
    "Reduce DSO By (Days)",
    0,
    30,
    5
)

dpo_increase = st.sidebar.slider(
    "Increase DPO By (Days)",
    0,
    30,
    0
)

# ==========================================
# TABS
# ==========================================

tab1,tab2,tab3,tab4,tab5,tab6,tab7,tab8,tab9,tab10 = st.tabs([
    "Executive Summary",
    "Forecasting",
    "Benchmarking",
    "Gap Analysis",
    "Opportunity Ranking",
    "Scenario Simulator",
    "Value Creation",
    "Sensitivity Analysis",
    "DSO Discount Simulator",
    "DIO Optimiser Simulator"
])

# ======================================================
# TAB 1 : EXECUTIVE SUMMARY
# ======================================================

with tab1:

    st.subheader("Executive KPI Summary")

    c1,c2,c3,c4 = st.columns(4)

    c1.metric(
        "FY2026 Revenue",
        f"₹{forecast_revenue:,.2f} Mn"
    )

    c2.metric(
        "Forecast CCC",
        f"{forecast_ccc:.2f} Days"
    )

    c3.metric(
        "Benchmark CCC",
        f"{benchmark_ccc:.2f} Days"
    )

    c4.metric(
        "CCC Gap",
        f"{gap_ccc:.2f} Days"
    )

    st.markdown("---")

    d1,d2,d3,d4 = st.columns(4)

    d1.metric(
        "Receivables",
        f"₹{forecast_receivables:,.2f} Mn"
    )

    d2.metric(
        "Inventory",
        f"₹{forecast_inventory:,.2f} Mn"
    )

    d3.metric(
        "Payables",
        f"₹{forecast_payables:,.2f} Mn"
    )

    d4.metric(
        "Net Working Capital",
        f"₹{working_capital_requirement:,.2f} Mn"
    )

    st.markdown("### Working Capital Drivers")

    wc_df = pd.DataFrame({
        "Component":[
            "Receivables",
            "Inventory",
            "Payables"
        ],
        "Value":[
            forecast_receivables,
            forecast_inventory,
            -forecast_payables
        ]
    })

    fig = px.bar(
        wc_df,
        x="Component",
        y="Value",
        text="Value",
        color="Component",
        title="Working Capital Requirement Drivers"
    )

    fig.update_traces(
        texttemplate="₹%{y:,.0f}",
        textposition="outside"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.success(
        f"""
✅ Forecast Revenue : ₹{forecast_revenue:,.2f} Mn

✅ Forecast DSO : {forecast_dso:.2f} Days

✅ Forecast DIO : {forecast_dio:.2f} Days

✅ Forecast DPO : {forecast_dpo:.2f} Days

✅ Forecast CCC : {forecast_ccc:.2f} Days

✅ Net Working Capital Requirement : ₹{working_capital_requirement:,.2f} Mn
"""
    )

# ======================================================
# TAB 2
# ======================================================

with tab2:

    st.subheader("Forecast Summary")

    final_forecast = pd.DataFrame({
        "Financial Year":[
            "FY2026F",
            "FY2027F",
            "FY2028F"
        ],
        "Revenue (M)":[
            8965.84,
            9665.21,
            10364.58
        ],
        "DSO":[122.13]*3,
        "DIO":[248.18]*3,
        "DPO":[135.81]*3,
        "CCC":[234.50]*3
    })

    st.dataframe(
        final_forecast,
        use_container_width=True,
        hide_index=True
    )
# ======================================================
# TAB 3
# ======================================================

with tab3:

    benchmark_display = benchmark_df.copy()

    benchmark_display.index = range(
        1,
        len(benchmark_display) + 1
    )

    st.dataframe(
        benchmark_display,
        use_container_width=True
    )

    fig = px.bar(
        benchmark_df,
        x="Company",
        y="Avg CCC",
        color="Avg CCC",
        text="Avg CCC",
        color_continuous_scale="RdYlGn_r",
        title="Peer CCC Benchmarking"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ======================================================
# TAB 4
# ======================================================

with tab4:

    gap_table = pd.DataFrame({
        "Metric":[
            "DSO",
            "DIO",
            "DPO",
            "CCC"
        ],
        "Benchmark":[
            91.19,
            177.83,
            119.49,
            149.54
        ],
        "Centum":[
            113.94,
            269.70,
            130.93,
            252.72
        ],
        "Gap":[
            22.75,
            91.87,
            11.44,
            103.18
        ]
    })

    st.dataframe(
        gap_table,
        use_container_width=True,
hide_index=True
    )

# ======================================================
# TAB 5
# ======================================================

with tab5:

    opportunity_df = pd.DataFrame({
        "Driver":[
            "DIO",
            "DSO",
            "DPO"
        ],
        "Opportunity":[
            91.87,
            22.75,
            -11.44
        ]
    })

    fig = px.bar(
        opportunity_df,
        x="Driver",
        y="Opportunity",
        text="Opportunity",
        color="Opportunity",
        title="Opportunity Ranking Across CCC Drivers"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ======================================================
# TAB 6
# ======================================================

with tab6:

    revised_ccc = (
        (forecast_dso - dso_reduction)
        +
        (forecast_dio - dio_reduction)
        -
        (forecast_dpo + dpo_increase)
    )

    ccc_reduction = (
        forecast_ccc - revised_ccc
    )

    scenario_df = pd.DataFrame({
        "Metric":[
            "Current CCC",
            "Optimized CCC",
            "Reduction"
        ],
        "Value":[
            forecast_ccc,
            revised_ccc,
            ccc_reduction
        ]
    })

    st.dataframe(
        scenario_df,
        use_container_width=True,
hide_index=True
    )

# ======================================================
# TAB 7
# ======================================================

with tab7:

    cash_release = (
        forecast_revenue / 360
    ) * ccc_reduction

    interest_saved = (
        cash_release
        * interest_rate
        / 100
    )

    k1,k2,k3,k4 = st.columns(4)

    k1.metric(
        "Optimized CCC",
        f"{revised_ccc:.2f}"
    )

    k2.metric(
        "CCC Reduction",
        f"{ccc_reduction:.2f} Days"
    )

    k3.metric(
        "Cash Released",
        f"₹{cash_release:,.2f} Mn"
    )

    k4.metric(
        "Interest Savings",
        f"₹{interest_saved:,.2f} Mn"
    )

# ======================================================
# TAB 8
# ======================================================

with tab8:

    sensitivity_df = pd.DataFrame({
        "Company":[
            "Centum",
            "Astra",
            "Datapatterns",
            "Kaynes Technologies",
            "Apollo Micro Systems"
        ],
        "Avg CCC":[
            252.72,
            422.08,
            868.91,
            149.54,
            489.20
        ],
        "Rank (All Data)":[
            2,3,5,1,4
        ],
        "Avg9 CCC":[
            261.15,
            444.35,
            706.91,
            149.54,
            517.11
        ],
        "Rank (9Y)":[
            2,3,5,1,4
        ]
    })

    st.dataframe(
        sensitivity_df,
        use_container_width=True,
hide_index=True
    )
# ======================================================
# TAB 9 : DSO DISCOUNT SIMULATOR
# ======================================================

with tab9:

    st.subheader("DSO Discount Scenario Analysis")

    col1, col2 = st.columns(2)

    with col1:

        forecast_revenue = st.number_input(
            "FY2026 Revenue (₹ Mn)",
            min_value=1.0,
            value=float(final_forecast.loc[0, "Revenue (M)"])
        )

        current_dso = st.number_input(
            "Current DSO (Days)",
            min_value=1.0,
            value=float(final_forecast.loc[0, "DSO"])
        )

    with col2:

        benchmark_dso = st.number_input(
            "Benchmark DSO (Days)",
            min_value=1.0,
            value=86.86
        )

        discount_rate = st.number_input(
            "Cash Discount (%)",
            min_value=0.0,
            max_value=20.0,
            value=2.0
        )

    borrowing_rate = interest_rate

    # =====================================================
    # RECEIVABLE GAP ANALYSIS
    # =====================================================

    current_receivables = (
        forecast_revenue *
        current_dso /
        360
    )

    benchmark_receivables = (
        forecast_revenue *
        benchmark_dso /
        360
    )

    excess_receivables = (
        current_receivables -
        benchmark_receivables
    )

    dso_gap = (
        current_dso -
        benchmark_dso
    )

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Current Receivables",
        f"₹{current_receivables:,.2f} Mn"
    )

    c2.metric(
        "Benchmark Receivables",
        f"₹{benchmark_receivables:,.2f} Mn"
    )

    c3.metric(
        "Excess Receivables",
        f"₹{excess_receivables:,.2f} Mn"
    )

    st.info(
        f"""
DSO Gap = {dso_gap:.2f} Days

Receivables locked above benchmark = ₹{excess_receivables:,.2f} Mn
"""
    )

    # =====================================================
    # DSO SCENARIO ANALYSIS
    # =====================================================

    acceptance_levels = [20, 40, 60, 80, 100]

    scenario_results = []

    for acceptance in acceptance_levels:

        acceptance_factor = acceptance / 100

        cash_released = (
            excess_receivables *
            acceptance_factor
        )

        dso_reduced = (
            dso_gap *
            acceptance_factor
        )

        new_dso = (
            current_dso -
            dso_reduced
        )

        discount_expense = (
            cash_released *
            discount_rate /
            100
        )

        interest_saved = (
            cash_released *
            borrowing_rate /
            100
        )

        total_benefit = (
            interest_saved -
            discount_expense
        )

        roi = (
            total_benefit /
            discount_expense * 100
            if discount_expense > 0
            else 0
        )

        scenario_results.append({

            "Scenario":
            f"{acceptance}% Acceptance",

            "Cash Released (₹ Mn)":
            round(cash_released, 2),

            "DSO Reduced":
            round(dso_reduced, 2),

            "New DSO":
            round(new_dso, 2),

            "Discount Expense":
            round(discount_expense, 2),

            "Interest Saved":
            round(interest_saved, 2),

            "Net Benefit":
            round(total_benefit, 2),

            "ROI (%)":
            round(roi, 2)
        })

    dso_scenario = pd.DataFrame(
        scenario_results
    )

    st.markdown(
        "### Scenario Results"
    )

    st.dataframe(
        dso_scenario,
        use_container_width=True,
        hide_index=True
    )

    # =====================================================
    # BENEFIT CHART
    # =====================================================

    fig = px.bar(
        dso_scenario,
        x="Scenario",
        y=[
            "Cash Released (₹ Mn)",
            "Net Benefit"
        ],
        barmode="group",
        title="Cash Released vs Net Benefit"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # =====================================================
    # ROI CHART
    # =====================================================

    roi_fig = px.line(
        dso_scenario,
        x="Scenario",
        y="ROI (%)",
        markers=True,
        title="ROI Across Acceptance Scenarios"
    )

    st.plotly_chart(
        roi_fig,
        use_container_width=True
    )

    best_case = dso_scenario.iloc[-1]

    st.success(
        f"""
✅ Current DSO : {current_dso:.2f} Days

✅ Benchmark DSO : {benchmark_dso:.2f} Days

✅ DSO Gap : {dso_gap:.2f} Days

✅ Excess Receivables : ₹{excess_receivables:,.2f} Mn

✅ At 100% Acceptance

• Cash Released : ₹{best_case['Cash Released (₹ Mn)']:,.2f} Mn

• DSO Reduction : {best_case['DSO Reduced']:.2f} Days

• New DSO : {best_case['New DSO']:.2f} Days

• Discount Expense : ₹{best_case['Discount Expense']:,.2f} Mn

• Interest Saved : ₹{best_case['Interest Saved']:,.2f} Mn

• Net Benefit : ₹{best_case['Net Benefit']:,.2f} Mn

• ROI : {best_case['ROI (%)']:.2f}%
"""
    )
# ======================================================
# RECOMMENDATION
# ======================================================

st.markdown("---")

st.subheader("Executive Recommendation")

st.success(
f"""
✅ Inventory Optimization remains the highest-priority lever.

✅ Current Forecast CCC: {forecast_ccc:.2f} Days

✅ Optimized CCC: {revised_ccc:.2f} Days

✅ Cash Release Potential: ₹{cash_release:,.2f} Mn

✅ Interest Savings Potential: ₹{interest_saved:,.2f} Mn

✅ Recommended Focus:
Inventory Optimization (DIO) followed by Receivables Optimization (DSO).
"""
)
# ======================================================
# DIO SCENARIO ANALYSIS
# ======================================================

with tab10:

    st.subheader("Inventory Optimization Scenario Analysis")

    col1, col2 = st.columns(2)

    with col1:

        forecast_revenue = st.number_input(
            "FY2026 Revenue (₹ Mn)",
            min_value=1.0,
            value=float(final_forecast.loc[0, "Revenue (M)"]),
            key="dio_revenue"
        )

        current_dio = st.number_input(
            "Current DIO (Days)",
            min_value=1.0,
            value=float(final_forecast.loc[0, "DIO"]),
            key="current_dio"
        )

    with col2:

        benchmark_dio = st.number_input(
            "Benchmark DIO (Days)",
            min_value=1.0,
            value=175.62,
            key="benchmark_dio"
        )

        carrying_cost_rate = st.number_input(
            "Inventory Carrying Cost (%)",
            min_value=0.0,
            max_value=20.0,
            value=3.0,
            key="carrying_cost"
        )

    financing_cost_rate = interest_rate

    # =====================================================
    # INVENTORY GAP ANALYSIS
    # =====================================================

    current_inventory = (
        forecast_revenue *
        current_dio /
        360
    )

    benchmark_inventory = (
        forecast_revenue *
        benchmark_dio /
        360
    )

    excess_inventory = (
        current_inventory -
        benchmark_inventory
    )

    dio_gap = (
        current_dio -
        benchmark_dio
    )

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Current Inventory",
        f"₹{current_inventory:,.2f} Mn"
    )

    c2.metric(
        "Benchmark Inventory",
        f"₹{benchmark_inventory:,.2f} Mn"
    )

    c3.metric(
        "Excess Inventory",
        f"₹{excess_inventory:,.2f} Mn"
    )

    st.info(
        f"""
DIO Gap = {dio_gap:.2f} Days

Inventory locked above benchmark = ₹{excess_inventory:,.2f} Mn
"""
    )

    # =====================================================
    # SCENARIO ANALYSIS
    # =====================================================

    acceptance_levels = [20, 40, 60, 80, 100]

    scenario_results = []

    for acceptance in acceptance_levels:

        acceptance_factor = acceptance / 100

        inventory_released = (
            excess_inventory *
            acceptance_factor
        )

        dio_reduced = (
            dio_gap *
            acceptance_factor
        )

        new_dio = (
            current_dio -
            dio_reduced
        )

        financing_saved = (
            inventory_released *
            financing_cost_rate /
            100
        )

        carrying_saved = (
            inventory_released *
            carrying_cost_rate /
            100
        )

        total_benefit = (
            financing_saved +
            carrying_saved
        )

        roi = (
            total_benefit /
            inventory_released * 100
            if inventory_released > 0
            else 0
        )

        scenario_results.append({

            "Scenario":
            f"{acceptance}% Implementation",

            "Inventory Released (₹ Mn)":
            round(inventory_released, 2),

            "DIO Reduced":
            round(dio_reduced, 2),

            "New DIO":
            round(new_dio, 2),

            "Financing Benefit":
            round(financing_saved, 2),

            "Carrying Benefit":
            round(carrying_saved, 2),

            "Total Benefit":
            round(total_benefit, 2),

            "ROI (%)":
            round(roi, 2)
        })

    dio_scenario = pd.DataFrame(
        scenario_results
    )

    st.markdown("### Scenario Results")

    st.dataframe(
        dio_scenario,
        use_container_width=True,
        hide_index=True
    )

    # =====================================================
    # BENEFIT CHART
    # =====================================================

    fig = px.bar(
        dio_scenario,
        x="Scenario",
        y=[
            "Inventory Released (₹ Mn)",
            "Total Benefit"
        ],
        barmode="group",
        title="Inventory Release vs Total Benefit"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # =====================================================
    # ROI CHART
    # =====================================================

    roi_fig = px.line(
        dio_scenario,
        x="Scenario",
        y="ROI (%)",
        markers=True,
        title="ROI Across Implementation Levels"
    )

    st.plotly_chart(
        roi_fig,
        use_container_width=True
    )

    best_case = dio_scenario.iloc[-1]

    st.success(
        f"""
✅ Current DIO : {current_dio:.2f} Days

✅ Benchmark DIO : {benchmark_dio:.2f} Days

✅ DIO Gap : {dio_gap:.2f} Days

✅ Excess Inventory : ₹{excess_inventory:,.2f} Mn

✅ At 100% Implementation

• Inventory Released : ₹{best_case['Inventory Released (₹ Mn)']:,.2f} Mn

• DIO Reduction : {best_case['DIO Reduced']:.2f} Days

• New DIO : {best_case['New DIO']:.2f} Days

• Financing Benefit : ₹{best_case['Financing Benefit']:,.2f} Mn

• Carrying Benefit : ₹{best_case['Carrying Benefit']:,.2f} Mn

• Total Benefit : ₹{best_case['Total Benefit']:,.2f} Mn

• ROI : {best_case['ROI (%)']:.2f}%
"""
    )
import streamlit as st
import time
from algorithms.bubblesort import bubble_sort
from algorithms.insertionsort import insertion_sort
from algorithms.mrgesort import merge_sort
from algorithms.timsort import timsort

st.set_page_config(page_title="Algorithm Visualiser", layout="wide")

st.title("Algorithm Visualizer")
st.markdown("<p style='text-align: center;'>Watch how algorithms sort your data – numbers or text!</p>", unsafe_allow_html=True)

chart_area = st.empty()
comparison_display = st.empty()

user_input = st.text_input("Enter comma-separated values", "5,3,8,1,2")
algorithm = st.selectbox("Choose algorithm", ["Bubble Sort", "Insertion Sort", "Merge Sort", "Tim Sort"])

algo_desc = {
    "Bubble Sort": "Bubble Sort repeatedly swaps adjacent elements to sort the list. Simple but slow for large data.",
    "Insertion Sort": "Insertion Sort builds the sorted list one element at a time by inserting into the correct position.",
    "Merge Sort": "Merge Sort recursively divides the list and merges sorted sublists. Efficient O(n log n) algorithm.",
    "Tim Sort": "TimSort splits the list into small runs, sorts each run with Insertion Sort, then merges runs like Merge Sort. Python's default sort."
}

speed = st.slider("⚡ Speed", 1, 10, 5)
delay = 1.1 - (speed * 0.1)

st.markdown(algo_desc[algorithm])

if st.button("▶️ Run Algorithm"):
    items = [x.strip() for x in user_input.split(",")]
    is_numeric = all(item.replace("-", "").isnumeric() for item in items)
    arr = [int(x) for x in items] if is_numeric else items

    if algorithm == "Bubble Sort":
        steps, total_comparisons = bubble_sort(arr.copy())
    elif algorithm == "Insertion Sort":
        steps = insertion_sort(arr.copy())
    elif algorithm == "Merge Sort":
        steps, total_comparisons = merge_sort(arr.copy())
    else:  # Tim Sort
        steps, total_comparisons = timsort(arr.copy())
    comparison_count = 0

    for index, (state, highlights) in enumerate(steps):
        is_comparison = index % 2 == 0
        if is_comparison:
            comparison_count += 1

        highlight_set = set(highlights)
        chart_html = ""
        for i, val in enumerate(state):
            color = "#e74c3c" if i in highlight_set else "#3498db"
            chart_html += f"""
                <div style="display:inline-block; width:30px; margin:2px; background:{color}; height:100px; text-align:center; vertical-align:bottom;">
                    <div style="transform: rotate(0deg); color:white; padding-top:70px;">{val}</div>
                </div>
            """

        chart_area.markdown(chart_html, unsafe_allow_html=True)
        comparison_display.markdown(f"🔁 Comparisons: **{comparison_count}**")
        time.sleep(delay)

    st.success("🎉 Done! Sorted successfully.")

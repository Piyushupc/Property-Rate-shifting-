import tkinter as tk
from tkinter import filedialog, ttk, messagebox
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import seaborn as sns
from Graph import plot_avg_price_by_city
from Main import run_models
from Graph import *  # (optional if you made functions)


df = None  

def load_file():
    """Load dataset"""
    global df
    file_path = filedialog.askopenfilename(
        title="Select CSV File", filetypes=[("CSV Files", "*.csv")]
    )
    if file_path:
        try:
            df = pd.read_csv(file_path)
            df = df.loc[:, ~df.columns.str.contains("^Unnamed")]
            messagebox.showinfo("Loaded", "Dataset loaded successfully!")
            update_city_list()
        except Exception as e:
            messagebox.showerror("Error", f"Could not load file:\n{e}")

def update_city_list():
    """Update city dropdown"""
    if "City" in df.columns:
        cities = sorted(df["City"].dropna().unique())
        city_box["values"] = ["All"] + list(cities)
        city_box.current(0)

def show_plot():
    """Show selected graph"""
    if df is None:
        messagebox.showwarning("Warning", "Please load dataset first.")
        return

    graph = graph_box.get()
    city = city_box.get()
    temp = df.copy()

    if city != "All":
        temp = temp[temp["City"] == city]

    plt.close("all")
    fig, ax = plt.subplots(figsize=(7, 5))

    try:
        if graph == "Line: SqFt vs Price":
            ax.plot(temp["Square_Feet"], temp["Price_Per_SqFt"], color="blue")
            ax.set_xlabel("Square Feet")
            ax.set_ylabel("Price per SqFt")
            ax.set_title(f"{city} - Line Graph")

        elif graph == "Bar: Avg Price by City":
            avg = temp.groupby("City")["Price_Per_SqFt"].mean().sort_values()
            avg.plot(kind="bar", color="green", ax=ax)
            ax.set_title("Average Price per SqFt by City")

        elif graph == "Histogram: Price Distribution":
            ax.hist(temp["Price_Per_SqFt"], bins=30, color="purple", edgecolor="black")
            ax.set_xlabel("Price per SqFt")
            ax.set_ylabel("Count")
            ax.set_title("Price Distribution")

        elif graph == "Scatter: SqFt vs Price":
            ax.scatter(temp["Square_Feet"], temp["Price_Per_SqFt"], color="red", alpha=0.6)
            ax.set_xlabel("Square Feet")
            ax.set_ylabel("Price per SqFt")
            ax.set_title("Scatter Plot")

        elif graph == "Pie: Properties by City":
            counts = temp["City"].value_counts()
            counts.plot.pie(autopct="%1.1f%%", startangle=90, ax=ax)
            ax.set_ylabel("")
            ax.set_title("Property Distribution by City")

        elif graph == "Heatmap: Correlation":
            corr = temp.corr(numeric_only=True)
            sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)
            ax.set_title("Feature Correlation")

        # Display on GUI
        for w in plot_frame.winfo_children():
            w.destroy()
        canvas = FigureCanvasTkAgg(fig, master=plot_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    except Exception as e:
        messagebox.showerror("Error", f"Could not draw graph:\n{e}")

# ---------------- GUI -----------------
root = tk.Tk()
root.title("Real Estate Price Visualizer")
root.geometry("950x650")

top_frame = tk.Frame(root)
top_frame.pack(pady=10)

load_btn = tk.Button(top_frame, text="Load CSV", command=load_file)
load_btn.grid(row=0, column=0, padx=10)

tk.Label(top_frame, text="City:").grid(row=0, column=1)
city_box = ttk.Combobox(top_frame, width=15, state="readonly")
city_box.grid(row=0, column=2, padx=10)

tk.Label(top_frame, text="Graph:").grid(row=0, column=3)
graph_box = ttk.Combobox(
    top_frame,
    width=30,
    state="readonly",
    values=[
        "Line: SqFt vs Price",
        "Bar: Avg Price by City",
        "Histogram: Price Distribution",
        "Scatter: SqFt vs Price",
        "Pie: Properties by City",
        "Heatmap: Correlation",
    ],
)
graph_box.current(0)
graph_box.grid(row=0, column=4, padx=10)

plot_btn = tk.Button(top_frame, text="Show Graph", command=show_plot)
plot_btn.grid(row=0, column=5, padx=10)

plot_frame = tk.Frame(root, bd=2, relief="sunken")
plot_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

root.mainloop()

def run_analysis():
    results = run_models()
    if "error" in results:
        messagebox.showerror("Error", results["error"])
    else:
        msg = f"Linear Regression:\nMSE = {results['MSE']:.2f}\nR² = {results['R2']:.2f}"
        messagebox.showinfo("Model Results", msg)


analyze_btn = tk.Button(top_frame, text="Run Analysis", command=run_analysis)
analyze_btn.grid(row=1, column=0, columnspan=6, pady=10)


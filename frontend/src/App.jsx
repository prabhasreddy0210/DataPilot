import { useState } from "react";
import "./App.css";

function App() {
  const [question, setQuestion] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const [activePage, setActivePage] = useState("dashboard");
  const [databaseData, setDatabaseData] = useState(null);

  const exampleQuestions = [
    "Show me all products costing more than 20000",
    "What is the total revenue?",
    "Show me the top 5 products by sales",
    "Which region has the highest sales?",
  ];

  const askDataPilot = async () => {
    if (!question.trim()) {
      return;
    }

    setLoading(true);
    setError("");
    setResult(null);

    try {
      const response = await fetch("http://127.0.0.1:8000/query", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          question: question,
        }),
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.detail || "Something went wrong");
      }

      setResult(data);
    } catch (error) {
      setError(error.message);
    } finally {
      setLoading(false);
    }
  };

  const loadDatabase = async () => {
    setError("");

    try {
      const [customersResponse, productsResponse, salesResponse] =
        await Promise.all([
          fetch("http://127.0.0.1:8000/customers"),
          fetch("http://127.0.0.1:8000/products"),
          fetch("http://127.0.0.1:8000/sales"),
        ]);

      if (
        !customersResponse.ok ||
        !productsResponse.ok ||
        !salesResponse.ok
      ) {
        throw new Error("Unable to load database information.");
      }

      const customers = await customersResponse.json();
      const products = await productsResponse.json();
      const sales = await salesResponse.json();

      setDatabaseData({
        customers,
        products,
        sales,
      });

      setActivePage("database");
    } catch (error) {
      setError(error.message);
    }
  };

  const showHistory = () => {
    setActivePage("history");
    setError("");
  };

  const showDashboard = () => {
    setActivePage("dashboard");
    setError("");
  };

  return (
    <div className="app">

      {/* SIDEBAR */}
      <aside className="sidebar">

        <div className="logo">
          <div className="logo-icon">D</div>
          <span>DataPilot</span>
        </div>

        <nav>

          <div
            className={`nav-item ${
              activePage === "dashboard" ? "active" : ""
            }`}
            onClick={showDashboard}
          >
            <span>⌂</span>
            Dashboard
          </div>

          <div
            className={`nav-item ${
              activePage === "history" ? "active" : ""
            }`}
            onClick={showHistory}
          >
            <span>▣</span>
            Query History
          </div>

          <div
            className={`nav-item ${
              activePage === "database" ? "active" : ""
            }`}
            onClick={loadDatabase}
          >
            <span>◈</span>
            Database
          </div>

        </nav>

        <div className="sidebar-bottom">

          <div className="status-dot"></div>

          <div>
            <strong>Database connected</strong>
            <small>SQLite • Online</small>
          </div>

        </div>

      </aside>

      {/* MAIN */}
      <main className="main">

        {/* TOP BAR */}
        <header className="topbar">

          <div>
            <h1>
              {activePage === "dashboard" && "Analytics Dashboard"}
              {activePage === "database" && "Database"}
              {activePage === "history" && "Query History"}
            </h1>

            <p>
              {activePage === "dashboard" &&
                "Ask questions about your data using natural language."}

              {activePage === "database" &&
                "Explore the data available in your database."}

              {activePage === "history" &&
                "View your previous DataPilot queries."}
            </p>
          </div>

          <div className="avatar">
            DP
          </div>

        </header>

        {/* ERROR */}
        {error && (
          <div className="error-box">
            <strong>Something went wrong</strong>
            <p>{error}</p>
          </div>
        )}

        {/* ================= DASHBOARD ================= */}
        {activePage === "dashboard" && (
          <>
            {/* QUERY CARD */}
            <section className="query-card">

              <div className="query-header">

                <div>
                  <span className="badge">
                    AI ANALYTICS
                  </span>

                  <h2>
                    What would you like to know?
                  </h2>
                </div>

                <div className="sparkle">
                  ✦
                </div>

              </div>

              <div className="input-wrapper">

                <textarea
                  value={question}
                  onChange={(event) =>
                    setQuestion(event.target.value)
                  }
                  placeholder="Ask anything about your database..."
                />

                <button
                  className="ask-button"
                  onClick={askDataPilot}
                  disabled={loading}
                >
                  {loading
                    ? "Analyzing..."
                    : "Ask DataPilot →"}
                </button>

              </div>

              {/* EXAMPLES */}
              <div className="examples">

                <span>Try asking:</span>

                {exampleQuestions.map(
                  (example, index) => (
                    <button
                      key={index}
                      onClick={() =>
                        setQuestion(example)
                      }
                    >
                      {example}
                    </button>
                  )
                )}

              </div>

            </section>

            {/* LOADING */}
            {loading && (
              <div className="loading-state">

                <div className="loader"></div>

                <h3>
                  Analyzing your data...
                </h3>

                <p>
                  DataPilot is generating and
                  validating your SQL query.
                </p>

              </div>
            )}

            {/* RESULTS */}
            {result && !loading && (
              <div className="results-area">

                {/* SQL */}
                <section className="result-card">

                  <div className="section-title">

                    <span className="section-label">
                      GENERATED QUERY
                    </span>

                    <h3>
                      SQL
                    </h3>

                  </div>

                  <div className="sql-box">
                    <pre>
                      {result.sql}
                    </pre>
                  </div>

                </section>

                {/* TABLE */}
                <section className="result-card">

                  <div className="result-heading">

                    <div>
                      <span className="section-label">
                        QUERY RESULTS
                      </span>

                      <h3>
                        Data
                      </h3>
                    </div>

                    <span className="row-count">
                      {result.rows.length} rows
                    </span>

                  </div>

                  {result.rows.length > 0 ? (
                    <div className="table-wrapper">

                      <table>

                        <thead>

                          <tr>
                            {result.columns.map(
                              (column) => (
                                <th key={column}>
                                  {column}
                                </th>
                              )
                            )}
                          </tr>

                        </thead>

                        <tbody>

                          {result.rows.map(
                            (row, index) => (
                              <tr key={index}>

                                {result.columns.map(
                                  (column) => (
                                    <td key={column}>
                                      {String(
                                        row[column]
                                      )}
                                    </td>
                                  )
                                )}

                              </tr>
                            )
                          )}

                        </tbody>

                      </table>

                    </div>
                  ) : (
                    <div className="no-results">
                      Query executed successfully,
                      but no rows were returned.
                    </div>
                  )}

                </section>

              </div>
            )}

            {/* EMPTY STATE */}
            {!result &&
              !loading &&
              !error && (
                <div className="empty-state">

                  <div className="empty-icon">
                    ✦
                  </div>

                  <h2>
                    Turn questions into insights
                  </h2>

                  <p>
                    DataPilot uses AI to understand
                    your question, generate SQL, and
                    retrieve the answer from your
                    database.
                  </p>

                </div>
              )}

          </>
        )}

        {/* ================= DATABASE ================= */}
        {activePage === "database" && databaseData && (
          <section className="database-page">

            <div className="database-cards">

              <div className="database-card">
                <span>Customers</span>
                <strong>
                  {databaseData.customers.length}
                </strong>
              </div>

              <div className="database-card">
                <span>Products</span>
                <strong>
                  {databaseData.products.length}
                </strong>
              </div>

              <div className="database-card">
                <span>Sales</span>
                <strong>
                  {databaseData.sales.length}
                </strong>
              </div>

            </div>

            {/* PRODUCTS */}
            <section className="result-card">

              <span className="section-label">
                PRODUCTS
              </span>

              <h3>
                Products
              </h3>

              <div className="table-wrapper">

                <table>

                  <thead>
                    <tr>
                      <th>ID</th>
                      <th>Name</th>
                      <th>Category</th>
                      <th>Price</th>
                    </tr>
                  </thead>

                  <tbody>

                    {databaseData.products.map(
                      (product) => (
                        <tr key={product.id}>

                          <td>
                            {product.id}
                          </td>

                          <td>
                            {product.name}
                          </td>

                          <td>
                            {product.category}
                          </td>

                          <td>
                            ₹{product.price}
                          </td>

                        </tr>
                      )
                    )}

                  </tbody>

                </table>

              </div>

            </section>

            {/* CUSTOMERS */}
            <section className="result-card">

              <span className="section-label">
                CUSTOMERS
              </span>

              <h3>
                Customers
              </h3>

              <div className="table-wrapper">

                <table>

                  <thead>
                    <tr>
                      <th>ID</th>
                      <th>Name</th>
                      <th>Region</th>
                    </tr>
                  </thead>

                  <tbody>

                    {databaseData.customers.map(
                      (customer) => (
                        <tr key={customer.id}>

                          <td>
                            {customer.id}
                          </td>

                          <td>
                            {customer.name}
                          </td>

                          <td>
                            {customer.region}
                          </td>

                        </tr>
                      )
                    )}

                  </tbody>

                </table>

              </div>

            </section>

          </section>
        )}

        {/* ================= HISTORY ================= */}
        {activePage === "history" && (
          <section className="history-page">

            <div className="history-empty">

              <div className="empty-icon">
                ▣
              </div>

              <h2>
                Query History
              </h2>

              <p>
                Your previous queries will appear
                here.
              </p>

              <span>
                History storage will be added next.
              </span>

            </div>

          </section>
        )}

      </main>

    </div>
  );
}

export default App;
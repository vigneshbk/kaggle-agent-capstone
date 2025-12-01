
### Agentic AI based automated portfolio analyser.
Using agentic AI tool to connect to stock broker and retreieve the current holding.
Given below is the overall flow diagram of the agent.

![](https://www.googleapis.com/download/storage/v1/b/kaggle-user-content/o/inbox%2F1316584%2F28a1c36994b8f809eca5fe1aa11eca50%2Fviggs.drawio.png?generation=1764610616820414&alt=media)

 #### 🧩System Components and Agent Workflow

#### 1.User Prompt

- The entry point of the system.
- A user initiates a query related to their stock portfolio (e.g., “Summarize my holdings based on current market mood”).

#### 2.RootAgent
 - Acts as the orchestrator.
 - Receives the prompt and delegates tasks to specialized agents based on intent.

#### 3.MarketMoodAgent
- Tool Invoked: fetch_market_mood
- Purpose: Assesses current market sentiment.
- Data Source: TickerTape MarketAPI
- Output: Market mood indicators (e.g., bullish, bearish, neutral) used to contextualize portfolio performance.

#### 4.PortfolioExpert Agent
- Tool Invoked: 
- Purpose: Retrieves user's stock holdings.
- Data Source: Zerodha Kite API Server (connected to Zerodha Stock Broker)
- This is one of the core features of the agent it handles automatic login to zerodha stock broker using a browser login (Oauth). Then it set's up session and retrieves the stock holding for the llm to analyse in the future steps
- Output: Raw portfolio data including stock names, quantities, and valuations.


#### 5.SummarizerAgent
- Role: Synthesizes data from MarketMoodAgent and PortfolioExpert Agent.
- Generates a human-readable summary of the portfolio, factoring in market mood and holdings.
- Example Output: “Your portfolio is overweight in tech stocks, which may be volatile given current bearish sentiment.”



~~#### 6.SessionMemory & SessionStoreDB **- Not Implemented**~~
~~- Purpose: Persist session context and user data.
- SessionMemory: Temporarily holds data during active interaction.
- SessionStoreDB: Stores session history for future reference or audits.~~



#### 7.Final Output: Stock Portfolio Summary
- Delivered to the user.
- Combines market sentiment and personalized holdings data.
- Enables informed decision-making and portfolio adjustments.

**Google Gemini the Brains of the Agentic System**
- Role: Decision-making and routing logic.
- Bridges communication between MarketMoodAgent and PortfolioExpert Agent.
- May apply reasoning or optimization to determine next steps in the analysis pipeline.




 #### 🛠️ Key Design Principles
- Modularity: Each agent performs a distinct function, enabling scalability and maintainability.
- Real-Time Integration: Live data from market APIs and brokerage servers ensures up-to-date analysis.
- Contextual Intelligence: Market mood is used to interpret portfolio risk and performance.
- Session Persistence: Memory components allow continuity across user sessions.



###  🔐 Zerodha Kite OAuth Login Flow (Jupyter Notebook Integration)

The integration uses OAuth 2.0 to authenticate users and obtain an access token for Zerodha Kite API calls. The flow involves redirecting the user for login, capturing a request token, and exchanging it for an access token. Given below is the architecture/flow diagram

 ![](https://www.googleapis.com/download/storage/v1/b/kaggle-user-content/o/inbox%2F1316584%2F539ff4e1659d9a3bbaceff9a57b2e6d8%2Fzerodha-login.jpg?generation=1764611970382350&alt=media)

#### 🔄 Step-by-Step Flow

1. **Jupyter Notebook Initialization**
   - Starts a local HTTP server on `localhost:8080` to handle OAuth callbacks.

2. **Login Redirect**
   - Redirects the user to the Zerodha Kite Login Page via browser.

3. **User Authentication**
   - User logs in on the Zerodha Kite Login Page.
   - The login page communicates with the Zerodha Kite Server to validate credentials.

4. **Request Token Delivery**
   - Upon successful login, the Zerodha Kite Server redirects back to the Jupyter Notebook's callback URL.
   - The redirect URL contains a `request_token`.

5. **Token Exchange**
   - The Jupyter Notebook sends the `request_token` along with the registered `client_id` and `client_secret` to the Zerodha Kite Server.

6. **Access Token Response**
   - The Zerodha Kite Server returns an `access_token` (Auth Token).
   - This token is used for authenticated API calls to Zerodha Kite.

#### 🔧 Technical Notes

- **Port Used:** `8080` for local callback handling.
- **OAuth Credentials Required:** `client_id` and `client_secret` from Zerodha developer console.
- **Security:** Store tokens securely; avoid exposing them in notebooks or logs.
- **Libraries:** Typically uses the `kiteconnect` Python SDK for implementation.


Final Output of Agent

![](https://www.googleapis.com/download/storage/v1/b/kaggle-user-content/o/inbox%2F1316584%2Fb6584f57f9260b7ecb583b7180c826b6%2Fagent-outpout.png?generation=1764615049402040&alt=media)

# AI-Powered Product Recommendation System — Project Plan

## 1. Project Structure & Stack Choices

- **Frontend:** React (Vite or Create React App)
- **Backend:** Express.js (Node.js)
- **Data Storage:** No database — all data (products, users, user actions) will be mocked, handled in-memory, or with simple JSON files. Absolutely no real database will be used.
- **Authentication:** JWT-based (username/password)
- **Recommendation Engine:** Content-based filtering (with option to extend to collaborative filtering)
- **Testing:** Jest (backend), React Testing Library (frontend)

---

## 2. Feature Breakdown & Approach

### Backend (Express.js)
- **Serve Product Data:**
  - Load `mock_data.json` and expose endpoints for:
    - All products
    - Products by category/subcategory
    - Single product by ID
- **User Auth:**
  - JWT auth (register/login endpoints)
  - Store users in memory or a simple JSON file (no DB)
- **User Actions:**
  - Endpoints to record likes, views, purchases
  - Store in memory or a JSON file (no DB)
- **Recommendations:**
  - Endpoint to return recommended products for a user, based on:
    - User's likes/views/purchases (content-based: recommend similar products)
    - Optionally, simple collaborative filtering (users who liked X also liked Y)
- **Testing:**
  - Jest for API and recommendation logic

### Frontend (React)
- **Auth Pages:** Login/Register
- **Product Catalog:** List, filter, and search products; show categories
- **Product Detail:** Show product info, like/view/purchase buttons
- **Recommendations:** Show recommended products on home/profile page
- **User Actions:** Track and send likes/views/purchases to backend
- **Testing:** React Testing Library for UI

---

## 3. Development Steps

1. **Backend**
   - Set up Express server
   - Load `mock_data.json`
   - Implement product endpoints
   - Implement user auth (JWT, in-memory or JSON file)
   - Implement user action tracking (in-memory or JSON file)
   - Implement recommendation endpoint
   - Write backend tests

2. **Frontend**
   - Set up React app
   - Auth pages (login/register)
   - Product catalog and detail pages
   - Recommendation UI
   - User action buttons
   - Write frontend tests

3. **Documentation**
   - Brief README on setup, architecture, and how recommendations work

---

## 4. Why This Approach?
- **Simplicity:** No DB, just JSON files and in-memory data for everything
- **Speed:** Minimal setup, easy to run locally
- **Extensible:** Can swap in a real DB or more advanced recommendation logic later if needed
- **Meets All Requirements:** Auth, product catalog, recommendations, user tracking, tests — all without a real database

---

## 5. Next Steps
- Scaffold backend (Express, endpoints, JWT auth, product loading, user actions, recommendations — all in-memory or JSON file)
- Move to frontend (React app, UI, user actions, recommendations)
- Use TypeScript if desired for type safety (optional)

---

**This plan is designed for easy execution by Cursor or any developer, and does not require any real database.** 
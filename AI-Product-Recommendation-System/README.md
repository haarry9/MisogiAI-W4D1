# AI-Powered Product Recommendation System

## Overview
This project is a full-stack demo of an AI-powered product recommendation system. It features a React frontend and an Express.js backend, providing a seamless experience for product browsing, user actions, and personalized recommendations.

## Tech Stack
- **Frontend:** React (Vite)
- **Backend:** Express.js (Node.js)
- **Authentication:** JWT (username/password)
- **Recommendation Engine:** Content-based filtering (optionally collaborative)
- **Testing:** Jest (backend), React Testing Library (frontend)

## Setup & Running

### 1. Backend
- Go to the backend directory (see project structure).
- Install dependencies:
  ```bash
  pnpm install
  ```
- Start the server:
  ```bash
  pnpm start
  ```

### 2. Frontend
- Go to the frontend directory:
  ```bash
  cd frontend
  pnpm install
  pnpm run dev
  ```
- The app will be available at `http://localhost:5173` (default Vite port).

## Features
- **Product Catalog:** Browse, filter, and search products.
- **Auth:** Register/login with JWT.
- **User Actions:** Like, view, and purchase products (tracked per user).
- **Recommendations:** Personalized product recommendations based on your actions.

## How Recommendations Work
- The backend uses content-based filtering: it recommends products similar to those you've liked, viewed, or purchased.
- Optionally, collaborative filtering can be added (users who liked X also liked Y).

## Project Structure
- `frontend/` — React app
- `backend/` — Express server
- `mock_data.json` — Product data

--- 
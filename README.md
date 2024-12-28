 # Expression Drawing Processor API

This project provides a backend service for evaluating expressions drawn on a canvas. The system takes an image as input, processes the expression using the Gemini API, and fetches the appropriate result to present back to the end-user.

The backend is built using Python and leverages **FastAPI** and other major libraries such as **google-generative-ai**, **PIL (Pillow)**, **Pydantic**, and **Uvicorn** for its functionality.

## Features

- Accepts an image with a drawn expression.
- Processes the image and extracts the expression.
- Evaluate the expression using the **Gemini API**.
- Returns the calculated result to the user.
- Implements FastAPI for efficient and lightweight web services.
- Includes CORS middleware for cross-origin requests.
- Health-check route to monitor server uptime.

---

## Technology Stack

- **Python**: Backend programming language.
- **FastAPI**: Framework for building APIs.
- **Uvicorn**: ASGI server for running the FastAPI application.
- **Pillow (PIL)**: Library for image processing and manipulation.
- **Pydantic**: Data validation and settings management.
- **Google-Generative-AI**: Integration for advanced algorithms and data processing.

---

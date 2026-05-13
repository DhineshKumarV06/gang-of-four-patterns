Python Design Patterns Project

A beginner-friendly Python project demonstrating three widely used software design patterns:

- Factory Pattern
- Strategy Pattern
- Observer Pattern

These patterns help developers build scalable, maintainable, and reusable applications using clean object-oriented programming principles.

Overview

This project showcases practical implementations of common design patterns in Python.  
Each pattern is implemented in a separate file with simple real-world examples for easy understanding.

The project is useful for:

- Students learning Software Engineering or OOP
- Python beginners exploring design patterns
- Developers preparing for interviews
- Anyone wanting cleaner and more maintainable code

Design Patterns Implemented

1️⃣ Factory Pattern

The Factory Pattern is used to create objects without exposing the object creation logic to the client.

Example Used
- Email Notification
- SMS Notification

Benefits
- Loose coupling
- Cleaner object creation
- Easier code maintenance
- Better scalability

2️⃣ Strategy Pattern

The Strategy Pattern allows switching behaviors or algorithms dynamically at runtime.

Example Used
- Credit Card Payment
- UPI Payment
- PayPal Payment

Benefits
- Flexible behavior switching
- Eliminates large `if-else` conditions
- Improves code organization
- Easier to extend with new strategies

3️⃣ Observer Pattern

The Observer Pattern enables event-driven communication between objects.

Example Used
- YouTube Channel Notifications
- Subscriber Updates

Benefits
- Event-driven architecture
- Decoupled communication
- Easy notification handling
- Supports multiple subscribers/listeners

Project Structure

text
project/
│
├── factory_pattern.py
├── strategy_pattern.py
├── observer_pattern.py
└── README.md

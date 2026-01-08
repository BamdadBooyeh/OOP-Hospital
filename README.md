# Hospital Appointment System – OOP Project

## Overview
This project implements an object-oriented **Hospital Appointment System** designed to model core hospital operations using clean software design principles. The system focuses on managing people, scheduling appointments, and coordinating interactions between doctors, nurses, and patients.

The project was developed with a strong emphasis on **UML-driven design**, object relationships, and real-world modeling.

## System Design
The architecture is based on a UML class diagram and follows a hierarchical and modular structure.

### Core Concepts
- A base `Person` class is used to represent shared attributes across hospital roles.
- Specialized roles (`Doctor`, `Nurse`, `Patient`) extend the base class.
- Appointments link patients and doctors at specific times.
- A central `Hospital` class manages all entities and coordinates system operations.

## Main Entities

### Person
Base class containing common attributes:
- Name
- Age
- Gender

### Doctor
Extends `Person` and includes:
- Medical specialization
- Availability time slots
- Ability to add available working hours

### Nurse
Extends `Person` and includes:
- Assigned doctor reference

### Patient
Extends `Person` and includes:
- Medical history records
- List of scheduled appointments
- Ability to add medical history entries

### Appointment
Represents a scheduled visit between:
- One patient
- One doctor
- A specific date and time

### Hospital
Central management class responsible for:
- Storing doctors, nurses, patients, and appointments
- Registering new entities
- Booking appointments between patients and doctors

## Object-Oriented Principles
The project applies fundamental OOP principles:
- **Inheritance**: Shared behavior through the `Person` base class
- **Encapsulation**: Each class manages its own state and logic
- **Composition**: Hospital aggregates doctors, nurses, patients, and appointments
- **Abstraction**: High-level hospital operations abstract internal object interactions

## UML Diagram
The system structure follows the UML design below:

- `Person` is the superclass of `Doctor`, `Nurse`, and `Patient`
- `Hospital` aggregates all system entities
- `Appointment` connects doctors and patients through composition

## Technologies
- Programming Language: Python
- Paradigm: Object-Oriented Programming
- Design Methodology: UML-based modeling

## Purpose
The goal of this project was to design a realistic hospital appointment system while strengthening skills in:
- Object-oriented design
- UML interpretation and implementation
- System modeling and software architecture

## Possible Extensions
- Persistent storage (database integration)
- Conflict checking for appointment scheduling
- User authentication and roles
- Graphical user interface
- Advanced reporting and analytics

## Author
Bamdad Booyeh

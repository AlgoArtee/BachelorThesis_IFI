# Testing System for AI and Automation Tools

This project focuses on developing and evaluating a robust testing system for analyzing the performance of traditional testing tools, intelligent AI agents, and Large Action Models (LAMs). The system provides a unified dashboard for monitoring and managing the testing process, using a prototype hospital management application, CuraNava, as a test bed.

CuraNava serves as a modular and scalable application that includes essential hospital management features such as patient management, appointment scheduling, medical test result management, and medicine inventory. Although future plans may involve implementing three quality levels for each feature (poor, medium, high), these levels are not currently available.

## Table of Contents
- [Testing System Features](#testing-system-features)
- [System Architecture](#system-architecture)
- [Project Structure](#project-structure)
- [Setup and Deployment](#setup-and-deployment)
- [Evaluation Methodologies](#evaluation-methodologies)
- [Contributing](#contributing)
- [License](#license)

---

## Testing System Features

### General
- Unified dashboard for managing tests and visualizing results
- Integration with traditional testing tools, AI agents, and LAMs
- Modular architecture to support multiple application types
- Exportable reports for test analysis

### CuraNava Prototype Features
- **Patient Management**: CRUD operations for patient profiles, advanced search, and audit logging
- **Appointment Scheduling**: Calendar views, automated reminders, and conflict detection
- **Medical Test Results**: Secure uploads, categorization, and notifications
- **Medicine Inventory**: Stock tracking, low-stock alerts, and reporting
- **Security**: Role-based access control and two-factor authentication

### Version Switching for Future Testing
- Planned feature: Toggle between poor, medium, and high-quality versions of each functionality to assess testing tool adaptability

---

## System Architecture

### Frontend
- **Technology**: React
- **Features**: Interactive dashboard for test and system monitoring

### Backend
- **Technology**: Node.js with Express
- **Features**: RESTful APIs for test execution and data exchange

### Database
- **Type**: SQL database
- **Features**: Structured schema for storing test data, audit logs, and application metadata

### Deployment
- **Platform**: (tba)
- **Version Control**: Git (branch management, regular updates)

---

## Project Structure

```
BachelorThesis_IFI/
├── curanava/                   # The Prototype App with Features to be Tested
├── testing_tools/              # The Testing Tools Applied to the Prototype
├── management/                 # Integration with services like JIRA, OpenAI, GitLab ...
├── assesment/                  # Assesment Tools and Scripts for comparing the different Testing Tools
├── shared_configs/             # Project Configurations (like database configs etc)
├── dashboard/                  # Visual Interface of the Testing Workflow
├── docs/                       # Documentation files and guides
└── README.md                   # Project overview
```

---

## Setup and Deployment

### Prerequisites
- Node.js
- SQL database (e.g., MySQL, PostgreSQL)
- Git

### Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd TestingSystem
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Set up the database:
   - Configure the database connection in `config/database.js`
4. Start the development server:
   ```bash
   npm run dev
   ```

### Deployment
- Configure the environment variables for the target cloud platform.
- Deploy using the platform-specific CLI or UI tools.

---

## Evaluation Methodologies

This system supports the evaluation of:
1. **Traditional Automation Tools**: Tools like Playwright for automated UI and functional testing.
2. **AI Agents**: Agents such as TestZeus Hercules for adaptive and intelligent test execution.
3. **Large Action Models (LAMs)**: Models like xLAM for dynamic and context-aware testing workflows.

---

## License

This project is licensed under the MIT License. See `LICENSE` for details.

# Graphical Python Debugger

## Overview
The **Graphical Python Debugger** is a network-enabled debugging tool designed to simplify the debugging process for Python applications. This application can be hosted on a local network, allowing multiple devices to participate collaboratively in debugging sessions. It also includes a diagram generation feature to provide a visual overview of the Python files within a specified directory.

---

## Features

### 1. **Directory Diagram Generation**
- Generates a graphical diagram of Python files in a given directory.
- Displays:
  - Functions
  - Classes (including attributes and methods)
  - Relationships between files.
- Enables source code viewing directly from the diagram.

### 2. **Experimentation Window**
- Allows users to execute Python code snippets for experimentation during debugging.
- Provides a sandbox environment to test isolated pieces of code.

### 3. **Debugger Shell**
- Facilitates step-by-step execution of Python files.
- Core functionalities include:
  - Setting breakpoints.
  - Stepping through code execution.
  - Viewing variable values and their stored information.
  - Inspecting source code.
  - Executing Python expressions during halted execution.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/graphical-python-debugger.git
   cd graphical-python-debugger
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python app.py
   ```

4. Access the debugger via your web browser at `http://<host_ip>:<port>`.

---

## Usage

### Starting a Debugging Session
1. Specify the directory containing Python files.
2. Use the generated diagram to:
   - Explore file relationships.
   - Navigate to specific source code.

### Experimentation Window
- Open the experimentation panel.
- Write and execute Python snippets to test logic or functionality.

### Debugger Shell
- Load the desired Python file.
- Set breakpoints by clicking on specific lines in the source code view.
- Use the controls to:
  - Step through the code.
  - Inspect and manipulate variables.
  - Execute custom Python expressions.

---

## Network Collaboration
- Host the debugger on a local network to allow other devices to connect.
- Collaborators can participate in debugging sessions and view/share updates in real-time.

---

## Contribution

### Reporting Issues
Feel free to open issues on the GitHub repository for bugs, feature requests, or general feedback.

### Pull Requests
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature/bugfix.
3. Commit your changes with clear messages.
4. Submit a pull request.

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contact
For questions or support, please reach out to curlejo.4career@gmail.com or submit an issue on GitHub.
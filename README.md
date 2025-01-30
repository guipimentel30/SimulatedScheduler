# SimulatedScheduler 🖥️

![License](https://img.shields.io/badge/license-MIT-blue)  
![Build Status](https://img.shields.io/badge/build-passing-green)  
![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)


## Overview
This project simulates a **process management system** in an multiprogramming operating system environment. The system manages processes using a **Round-Robin scheduling algorithm**, focusing on **CPU** and **memory resource allocation**.  

It is designed to handle a **large number of processes**, each requiring a specific amount of memory and CPU time. 

We have designed the system so that **each class mimics the behavior of real OS components**. This means that:  
- The **CPU class** simulates the core functionalities of a real CPU, including process execution, resource handling and interruption signs.  
- The **Memory class** manages allocation and paging like an OS memory manager.  
- The **Dispatcher class** schedules processes just like a real OS scheduler.  

This approach ensures an **accurate and practical** representation of how operating systems **actually handle process management**.


## Features
**Process Generation** : Processes are generated randomly generated following specific rules with random attributes, including CPU time requirements, I/O time, and memory usage.

**Round-Robin Scheduling**: Processes are scheduled using a Round-Robin algorithm with a quantum of 4 time units.

**Memory Management**: Memory is managed using a paging system, with processes being loaded into memory when there is enough space available and freed upon completion.

**Thread Management**: The system uses three threads to manage process generation, dispatching, and execution.

**Real-Time Simulation**: The system provides real-time feedback on the state of processes, CPUs, and memory usage.

## Simulated System Requirements
**CPUs**: 4

**Memory**: 32 GB RAM

## Project Structure
The project is organized into several modules, each handling a specific aspect of the system:

- **cpu.py**: Manages CPU operations and process execution.

- **process.py**: Defines the Process class, its attributes, states and methods. It is important to note that is follows a five states system.

- **despachante.py**: Implements the dispatcher logic for scheduling processes.

- **processTable.py**: Manages the process table.

- **geradoraDeProcessos.py**: Handles the generation of new processes.

- **memory.py**: Manages memory allocation and deallocation using a paging system.


## Simulation Workflow
- **Process Generation**: The GeradoraDeProcessos thread generates new processes and adds them to the new process queue.

- **Memory Allocation**: Processes are allocated memory if space is available and moved to the ready queue.

- **Process Scheduling**: The Despachante thread schedules processes from the ready queue to the CPUs using the Round-Robin algorithm.

- **Process Execution**: Processes execute on the CPUs, transitioning between CPU and I/O phases as defined.

- **Memory Deallocation**: Upon completion, processes are removed from memory, freeing up space for new processes.

- **Real-Time Feedback**: The system provides real-time updates on the state of processes, CPUs, and memory usage.


## The simulation provides detailed output for each time unit, including:

- The state of each CPU (idle or executing a process).

- The contents of the new, ready, auxiliary, and I/O queues.

- The amount of free memory available.

## Conclusion
This project provides a comprehensive simulation of a process management system, demonstrating key concepts in operating systems such as process scheduling, memory management, and thread synchronization. The real-time feedback and customizable parameters make it a valuable tool for understanding and experimenting with these concepts.

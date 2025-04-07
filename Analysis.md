**Central Blood Bank Management System - Requirement Analysis Document**

## **1. Introduction**
The Central Blood Bank Management System is designed to manage blood donations, donor registrations, and hospital requests. The system ensures blood donations adhere to medical guidelines and optimally distributes blood to hospitals based on patient urgency and geographical proximity.

## **2. Functional Requirements**
### **Donor Management**
- Donors must register with their **National ID, Name, City, and Email**.
- The system verifies eligibility based on:
  - A minimum **3-month gap** between donations.
  - A **negative blood virus test**.
- If rejected, an email is sent with the reason.
- If accepted, the donation is added to the **blood stock** with:
  - **Blood type (O, A, B, AB, +, -)**
  - **Blood bank city**
  - **Expiration date**

### **Blood Stock Management**
- Stores accepted blood donations with details.
- Automatically removes **expired blood**.

### **Hospital Request Management**
- Hospitals request blood specifying:
  - **Blood type**
  - **City**
  - **Patient urgency level (Immediate, Urgent, Normal)**
- The system processes a **minimum of 10 requests at a time**.
- Blood is allocated based on **proximity of stock to hospital and urgency level**.
- If stock is unavailable, notify the hospital.

### **Notification System**
- **Emails donors** for donation rejection.
- **Emails hospitals** for request confirmation or denial.

## **3. Non-Functional Requirements**
- **Performance**: The system must process hospital requests efficiently.
- **Security**: Donor personal data must be encrypted.
- **Scalability**: The system should handle multiple requests concurrently.
- **Usability**: Provide a web-based user interface for donors and hospitals.

## **4. Use Cases Overview**
### **Use Case 1: Donor Registration**
**Actors:** Donor, System  
**Steps:**
1. Donor enters personal details.
2. System validates data.
3. Donor is registered.

### **Use Case 2: Blood Donation Approval**
**Actors:** Donor, System  
**Steps:**
1. Donor attempts to donate.
2. System checks last donation date.
3. System verifies blood test.
4. If eligible, donation is added to stock.
5. If rejected, the donor is notified via email.

### **Use Case 3: Hospital Blood Request**
**Actors:** Hospital, System  
**Steps:**
1. Hospital submits a blood request.
2. System checks stock availability.
3. If available, blood is allocated.
4. If unavailable, the hospital is notified.

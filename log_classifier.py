def parse_log(log_line):
    fields = log_line.split()
    event_id = int(fields[5].split("=")[1])
    return event_id

def classify_event(event_id):
    if event_id == 4624:
        return "Successful Logon"
    elif event_id == 4625:
        return "Failed Logon — possible brute force"
    elif event_id == 4688:
        return "Process Creation — possible execution"
    else:
        return "Unknown Event"

def print_report(log_line, event_id, classification):
    print("="*40)
    print(f"{'EVENT CLASSIFICATION REPORT':^40}")
    print("="*40)
    print(f"Log Line   : {log_line}")
    print(f"Event ID   : {event_id}")
    print(f"Description: {classification}")
    print("="*40)

print("Welcome to SOC Log Classifier")
print("Type 'exit' to quit\n")

while True:
    user_input = input("Enter log line: ")
    
    if user_input.lower() == "exit":
        print("Exiting. Stay safe.")
        break
    
    try:
        event_id = parse_log(user_input)
        classification = classify_event(event_id)
        print_report(user_input, event_id, classification)
    except ValueError:
        print("[ERROR] Invalid log line — could not extract Event ID")
    except IndexError:
        print("[ERROR] Log line format incorrect — check your input")

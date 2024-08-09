import torch

def check_mps_status():
    if torch.backends.mps.is_available():
        print("MPS backend is available.")
        if torch.backends.mps.is_built():
            print("MPS backend is built.")
        else:
            print("MPS backend is not built.")
    else:
        print("MPS backend is not available.")
        
    # Check the default device
    print(f"Default device: {torch.device('mps') if torch.backends.mps.is_available() else torch.device('cpu')}")

if __name__ == "__main__":
    check_mps_status()
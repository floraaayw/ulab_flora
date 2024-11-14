import numpy as np
import matplotlib.pyplot as plt

def vertical(domain=2):
    # Define the domain for x from 0 to 2π
    x = np.linspace(0, domain * np.pi, 100)
    
    # Define h(x) = cos(x) and k(x) = sin(x)
    h_x = np.cos(x)
    k_x = np.sin(x)
    
    # Create subplots stacked vertically
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(6, 8))
    
    # Top subplot for h(x) = cos(x)
    ax1.plot(x, h_x, label='h(x) = cos(x)', color='blue')
    ax1.set_title("Cosine Function")
    ax1.set_xlabel("x")
    ax1.set_ylabel("h(x)")
    ax1.legend()
    
    # Bottom subplot for k(x) = sin(x)
    ax2.plot(x, k_x, label='k(x) = sin(x)', color='red')
    ax2.set_title("Sine Function")
    ax2.set_xlabel("x")
    ax2.set_ylabel("k(x)")
    ax2.legend()
    
    # Display the plot
    plt.tight_layout()
    plt.show()

def plot_left_right(domain=2):
    # Define the domain for x from 0 to 2π
    x = np.linspace(0, domain * np.pi, 100)
    
    # Define h(x) = cos(x) and k(x) = sin(x)
    h_x = np.cos(x)
    k_x = np.sin(x)
    
    # Create subplots side-by-side
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
    
    # Left subplot for h(x) = cos(x)
    ax1.plot(x, h_x, label='h(x) = cos(x)', color='blue')
    ax1.set_title("Cosine Function")
    ax1.set_xlabel("x")
    ax1.set_ylabel("h(x)")
    ax1.legend()
    
    # Right subplot for k(x) = sin(x)
    ax2.plot(x, k_x, label='k(x) = sin(x)', color='red')
    ax2.set_title("Sine Function")
    ax2.set_xlabel("x")
    ax2.set_ylabel("k(x)")
    ax2.legend()
    
    # Display the plot
    plt.tight_layout()
    plt.show()
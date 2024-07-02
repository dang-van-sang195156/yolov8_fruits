import numpy as transforms

transform = transforms.Compose([
        transforms.Resize((640,640)),
        transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))]) 
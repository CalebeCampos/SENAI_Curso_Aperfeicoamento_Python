
import time
from tqdm import tqdm
# executar no terminal: pip install tqdm

# exibindo uma barra de progresso
for i in tqdm(range(100), desc="Loading"):
    time.sleep(0.05)
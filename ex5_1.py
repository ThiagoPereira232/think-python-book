# Faza um script para ler a hora atual e converter em hora:min:seg

import time

times = time.asctime(time.localtime(time.time()))
print(times)

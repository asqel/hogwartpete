RESTART_SIGNAL = "**$RESTART SIGNAL$**"



class signal:
	def __init__(self, name : str, data : dict[str, any] = None) -> None:
		self.name = name
		self.data = (data if data else {})

SIGNALS : list[signal] = []


def send_signal(sig : signal) :
	SIGNALS.append(sig)


def pop_signal() -> signal:
	if not SIGNALS:
		return None
	return SIGNALS.pop(0)
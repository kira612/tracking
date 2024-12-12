import matplotlib.pyplot as plt

class DataVisualizer:
    def __init__(self):
        plt.ion()
        self.fig, self.ax = plt.subplots()

    def update_plot(self, tracks, speeds):
        self.ax.clear()
        for track in tracks:
            if track.is_confirmed():
                self.ax.scatter(track.to_tlbr()[0], track.to_tlbr()[1], label=f'ID {track.track_id}, Speed: {speeds[track.track_id]:.2f}')
        self.ax.legend()
        plt.draw()
        plt.pause(0.001)

import numpy as np
import simphony.core as core
import simphony.errors as errors
import simphony.DeviceLibrary.ebeam as dev
import simphony.simulation as sim

bg_in = core.ComponentInstance(dev.ebeam_gc_te1550)
bg_out = core.ComponentInstance(dev.ebeam_gc_te1550)
y1 = core.ComponentInstance(dev.ebeam_y_1550)
y2 = core.ComponentInstance(dev.ebeam_y_1550)
wg1 = core.ComponentInstance(dev.ebeam_wg_integral_1550, extras={'length':50e-6, 'ne':10.1, 'ng':1.3})
wg2 = core.ComponentInstance(dev.ebeam_wg_integral_1550, extras={'length':150e-6, 'ne':12.15, 'ng':-3.7})

c1 = [y1, y1, y2, y2, bg_in, bg_out]
p1 = [1, 2, 2, 1, 0, 0]
c2 = [wg1, wg2, wg1, wg2, y1, y2]
p2 = [0, 0, 1, 1, 0, 0]
con = zip(c1, p1, c2, p2)

nl = core.Netlist()
nl.load(con, formatter='ll')
simu = sim.Simulation(nl)

freq = simu.freq_array
zero2zero = np.log10(abs(simu.s_parameters()[:, 0, 0])**2)
zero2one = np.log10(abs(simu.s_parameters()[:, 0, 1])**2)
one2zero = abs(simu.s_parameters()[:, 1, 0])**2
one2one = abs(simu.s_parameters()[:, 1, 1])**2

# assert np.all(freq == expected['freq'])
# assert np.all(zero2zero == expected['zero2zero'])
# assert np.all(zero2one == expected['zero2one'])
# assert np.all(one2zero == expected['one2zero'])
# assert np.all(one2one == expected['one2one'])

import matplotlib.pyplot as plt
plt.subplot(221)
plt.plot(freq, zero2zero)
plt.subplot(222)
plt.plot(freq, zero2one)
plt.subplot(223)
plt.plot(freq, one2zero)
plt.subplot(224)
plt.plot(freq, one2one)
plt.suptitle("MZI")
plt.tight_layout()
plt.show()

dc = core.ComponentInstance(dev.ebeam_dc_te1550)
wg1 = core.ComponentInstance(dev.ebeam_wg_integral_1550, extras={'length':73.562196e-6})
wg2 = core.ComponentInstance(dev.ebeam_wg_integral_1550, extras={'length':73.112196e-6})
wg3 = core.ComponentInstance(dev.ebeam_wg_integral_1550, extras={'length':64.952196e-6})
wg4 = core.ComponentInstance(dev.ebeam_wg_integral_1550, extras={'length':65.932196e-6})

conn = [
    [dc, 1, wg1, 0],
    [dc, 0, wg2, 0],
    [dc, 3, wg3, 0],
    [dc, 2, wg4, 0],
]

nl = core.Netlist()
nl.load(conn)
simu = sim.Simulation(nl)

freq = simu.freq_array
zero2zero = np.log10(abs(simu.s_parameters()[:, 0, 0])**2)
zero2one = np.log10(abs(simu.s_parameters()[:, 0, 1])**2)
one2zero = abs(simu.s_parameters()[:, 0, 2])**2
one2one = abs(simu.s_parameters()[:, 0, 3])**2

import matplotlib.pyplot as plt
plt.subplot(221)
plt.plot(freq, zero2zero)
plt.subplot(222)
plt.plot(freq, zero2one)
plt.subplot(223)
plt.plot(freq, one2zero)
plt.subplot(224)
plt.plot(freq, one2one)
plt.suptitle("MZI")
plt.tight_layout()
plt.show()
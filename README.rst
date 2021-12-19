====================================================
 Early Dark Energy search within SPT-3G public data
====================================================

.. image:: https://img.shields.io/badge/arXiv-XXXX.XXXXX-red.svg
   :target: https://arxiv.org/abs/XXXX

This repository holds the ``yaml`` configuration files for `cobaya <https://cobaya.readthedocs.io>`_
to reproduce results from `La Posta et al. <https://arxiv.org/abs/XXXX>`_. We also provide a jupyter
notebook to redo the figures from the article (see. `notebooks/ede_spt.ipynb`_) as well as the LaTeX
source files for the article itself.

MCMC results
------------

You can download the Monte-Carlo Markov Chains following the different links below:

- `SPT-3G <https://portal.nersc.gov/cfs/sobs/users/alaposta/ede_spt/spt3g.tar.gz>`_: results from
  SPT-3G TE+EE data alone from 2020 data release (`Dutcher et al
  <https://arxiv.org/abs/2101.01684>`_)

- `SPT-3G + Planck 2018 TT ($\ell$ < 650)
  <https://portal.nersc.gov/cfs/sobs/users/alaposta/ede_spt/spt3g_p18tt650.tar.gz>`_: results from
  SPT-3G TE+EE data combined with Planck 2018 TT spectrum ($\ell < 650$)

- `SPT-3G + Planck 2018 TT ($\ell$ < 650) + BAO + Planck Lensing
  <https://portal.nersc.gov/cfs/sobs/users/alaposta/ede_spt/spt3g_p18tt650_bao_lensing.tar.gz>`_:
  results from SPT-3G TE+EE data combined with Planck 2018 TT spectrum ($\ell < 650$) + Planck CMB
  Lensing and BAO data (`6dF <https://arxiv.org/abs/1106.3366>`_, SDSS `DR7
  <https://arxiv.org/abs/1409.3242>`_/`DR12 <https://arxiv.org/abs/1607.03155>`_)

- `SPT-3G + ACT DR4 + Planck 2018 TT ($\ell$ < 650)
  <https://portal.nersc.gov/cfs/sobs/users/alaposta/ede_spt/spt3g_act_p18tt650.tar.gz>`_: results
  from SPT-3G TE+EE data combined with ACT `DR4 <https://arxiv.org/abs/2007.07289>`_ and Planck 2018
  TT spectrum ($\ell < 650$)

- `SPT-3G + Planck 2018 high-$\ell$ TT+TE+EE + Planck 2018 low-$\ell$ TT
  <https://portal.nersc.gov/cfs/sobs/users/alaposta/ede_spt/spt3g_p18full.tar.gz>`_: results from
  SPT-3G TE+EE data combined with the full set of Planck 2018 data

- `SPT-3G + ACT DR4 + Planck 2018 high-$\ell$ TT+TE+EE + Planck 2018 low-$\ell$ TT
  <https://portal.nersc.gov/cfs/sobs/users/alaposta/ede_spt/spt3g_act_p18full.tar.gz>`_: results
  from SPT-3G TE+EE data combined with ACT `DR4 <https://arxiv.org/abs/2007.07289>`_ and the full
  set of Planck 2018 data

- `ACT DR4 <https://portal.nersc.gov/cfs/sobs/users/alaposta/ede_spt/act.tar.gz>`_: results
  from ACT `DR4 <https://arxiv.org/abs/2007.07289>`_

- `ACT DR4 + Planck 2018 TT ($\ell$ < 650)
  <https://portal.nersc.gov/cfs/sobs/users/alaposta/ede_spt/act_p18tt650.tar.gz>`_: results from ACT
  `DR4 <https://arxiv.org/abs/2007.07289>`_ combined with Planck 2018 TT spectrum ($\ell < 650$)

- `Planck 2018 high-$\ell$ TT+TE+EE + Planck 2018 low-$\ell$ TT
  <https://portal.nersc.gov/cfs/sobs/users/alaposta/ede_spt/p18.tar.gz>`_: results from the full set
  of Planck 2018 data

Reproducing the analysis
------------------------

Given the ``yaml`` files, you can reproduce the whole analysis results using ``cobaya``. First you
can install the bunch of software needed by this analysis with the following command

.. code:: shell

   $ pip install git+https://github.com/alaposta/ede_spt.git

Then, you can install the data needed by the different likelihoods with ``cobaya-install``. For
instance, to download SPT-3G data you can do

.. code:: shell

   $ cobaya-install -p /where/to/store/data yaml/spt3g_camb.yaml

Basically every time you want to run MCMC, just start by installing the needed material with
``cobaya-install``. You can finally run the MCMC with ``cobaya`` by doing

.. code:: shell

   $ cobaya-run -p /where/to/store/data yaml/spt3g_camb.yaml

If you have a cluster of machines with MPI support, you can split the process into $n$ independant
processes by doing

.. code:: shell

   $ mpirun -n 4 cobaya-run -p /where/to/store/data yaml/spt3g_camb.yaml

See
https://cobaya.readthedocs.io/en/latest/installation.html?highlight=mpi#mpi-parallelization-optional-but-encouraged
for more details regarding MPI support (you will need to install ``mpi4py`` for instance).

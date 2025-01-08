import sys
import pyemu
import multiprocessing as mp

if __name__ == "__main__":
    mp.freeze_support()

    t_d = "hosaki_template"
    m_d = "hosaki_model_master_2"
    num_workers = 10
    sys.path.insert(0,t_d)

    from forward_run import hosaki_ppw_worker as ppw_function
    pyemu.os_utils.start_workers(t_d,"pestpp-mou","pest.pst",
                                    num_workers=num_workers,
                                    master_dir=m_d,worker_root='.',
                                    verbose=True,
                                    ppw_function=ppw_function)

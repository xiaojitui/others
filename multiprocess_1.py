import multiprocessing as mp
from functools import partial 
from tqdm import tqdm
from datetime import datetime

def process_files(file):
	xxxx
	with open('/results/record_%d.pkl' % kf, 'wb') as f:
        pickle.dump(record, f)
		
		
if __name__ == '__main__':
	
    Number_of_workers = 40 

    print("run the job")
    print('multiprocess %d tasks'%len(all_files))
    pool = mp.Pool(Number_of_workers)
    job = partial(process_files)
    for _ in pool.imap_unordered(job, tqdm(all_files, total = len(all_files))):
        pass
    pool.close()
    pool.join()

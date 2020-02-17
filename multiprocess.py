import multiprocessing as mp
from functools import partial 
from tqdm import tqdm
from datetime import datetime

def process_files(pdf_dict, kf):
	xxxx
	with open('/results/record_%d.pkl' % kf, 'wb') as f:
        pickle.dump(record, f)
		
		
if __name__ == '__main__':
	
	Number_of_workers = 40
    file_dict = {}
    for x in range(Number_of_workers):
        file_dict[x]=[]
    i=0
    for file in files:
        file_dict[i%Number_of_workers].append(file)
        i+=1


    print('multiprocess %d tasks'%len(file_dict))
    t0 = datetime.now()
    pool = mp.Pool(Number_of_workers)
    job = partial(process_files, file_dict)
    for _ in pool.imap_unordered(job, tqdm(range(Number_of_workers), total = Number_of_workers), chunksize = 1):
        pass
    pool.close()
    pool.join()
    
    
    allrecord = {}
    for i in tqdm(range(Number_of_workers)):
        with open('/iresults/record_%d.pkl' % i, 'rb') as f:
            record = pickle.load(f)
        allrecord.update(record)
    with open('./combined_result.pkl', 'wb') as f:
            pickle.dump(allrecord, f)
            
            
    print("Finished in ", datetime.now() - t0)

#!/usr/bin/env python
# coding: utf-8

# In[86]:


import numpy as np
import math 
import random

class Algoritma_genetika :
# membuat algoritma genetika
# misalkan ada persamaan a+2b+3c+4d = 30
# maka buat algoritma genetika untuk mencari nilai a,b,c, dan d

# jumlah_chorm = 6
# gen = ["a","b","c","d"]
# # nilai_gen={
# #     nilai_gen_1={#a
# # #     "a"='min_1' : 0, "a"='max_1' : 30,
# # #     "b"="c"="d"='min_2' : 0, "b"="c"="d"='max_2' : 10
# #     'min':0,
# #     'max':30
# #     }
# #     nilai_gen_2={#bcd
# #         'min':0,
# #         'max':10
# #     }
# # } #nilai per gen a<=30 b=c=d<=10

# 	nilai_per_gen = {
# 		'min' : 0,
# 		'max' : 30
# 	} #nilai per gen 0-30\

# crossover_rate=50/100
# mutasi_rate=10/100
# total_gen=24
# # total_gen     = (jumlah gen dalam chromosome) * jumlah populasi
# # = 4 * 6
# # = 24
# next_gen=np.arange(4)
# stop=False

# #inisialisasi chromosome random
# 	def __init__(self):
# 		#pembentukan chromosome random
# 		self.first_chrom = np.random.randint(low=self.nilai_per_gen['min'], high=self.nilai_per_gen['max'], size=(self.jum_chrom, len(self.gen)))
# 		print(self.first_chrom)
# 		print("====================================================================================")
# 		print("====================================================================================")

	jum_chrom = 6 #jumlah chromosome
	gen = ["a", "b", "c", "d"] #nilai gen abcd
	nilai_per_gen = {
		'min' : 0,
		'max' : 10
	} #nilai per gen 0-10
    
	crossover_rate = 50/100 #persen
	mutasi_rate = 10/100 #persen
	total_gen = 24
# total_gen     = (jumlah gen dalam chromosome) * jumlah populasi
# = 4 * 6
# = 24
	next_gen = np.arange(4)
	stop = False

#inisialisasi chromosome secara random    
	def __init__(self):
		self.first_chrom = np.random.randint(low=self.nilai_per_gen['min'], high=self.nilai_per_gen['max'], size=(self.jum_chrom, len(self.gen)))
		print("==================================================inisialisasi=================================================")
		print(self.first_chrom)
		print("---------------------------------------------------------------------------------------------------------------")

#evaluasi chromosome
	def evaluasi_chrom(self, chrom, generasi):
		# mencari fungsi objektif
		# fungsi_objektif(chromosome) = | (a+2b+3c+4d) – 30 |
		print("GENERASI ["+str(generasi)+"] ------")
		
		jum_chromo = len(chrom)
		o = np.arange(jum_chromo)   
		fitness = np.arange(jum_chromo, dtype='f')
		
		for x in range(len(chrom)):
		
			#FUNGSI OBJEKTIF 
			#fo=fungsi_objektif(chromosome[x])=o[x]
			fo = abs((chrom[x][0]+2*chrom[x][1]+3*chrom[x][2]+4*chrom[x][3])-30)
			o[x] = fo
			
			#SELEKSI CHROMOSOME, DAN MENCARI FITNESS
			fitn = 1/(fo+1)
			
			fitness[x] = fitn
			if(fitn == 1):
				self.stop = True
			print("CHROMOSOME {0} : {1}, fitness = {2}".format(x, np.array2string(chrom[x], separator=','), fitn))
		print("FITNESS SELESAI!!")
		print(o)
		
        
#probabilitas
		Probab = np.arange(jum_chromo, dtype='f')
		# print(fitness)
		total_fitness = fitness.sum() #rumus total fitness
		Probab = fitness / total_fitness #rumus mencari probabilitas
		print("Total fitness : {}".format(str(total_fitness)))
		print("Rata-rata fitness : {}".format(str(np.average(fitness))))
		print("Probabilitas : {}".format(np.array2string(Probab, separator=',')))
		print("Probabilitas Paling Tinggi : {}, Pada chromosome ke {}".format(Probab[Probab.argmax()], str(Probab.argmax())))
		print("CHROMOSOME YANG MUNGKIN TERPILIH : {}".format(np.array2string(chrom[Probab.argmax()], separator=',')))
		print("")
		print("")
		self.next_gen = chrom[Probab.argmax()]

#seleksi dengan ROULETE WHELL (C) dari cumulative probabilitas
		C = np.arange(jum_chromo, dtype='f')
		total_x = 0
		for x in range(len(Probab)):
			total_x += Probab[x]
			C[x] = total_x

#putar roulete whell sebanyak jumlah populasi yaitu 6 kali secara acak
		R = np.random.sample(len(fitness))
		chrom_baru = np.arange(jum_chromo*len(self.gen)).reshape(jum_chromo, len(self.gen))


#RUMUS UNTUK MENCARI CHROMOSOME BARU BERDASARKAN ROULETE WHELL
		for y in range(len(R)):
			for k in range(len(chrom_baru)):
				if(R[y] < C[0]):
					chrom_baru[y] = chrom[0]
				elif((C[k-1] < R[y]) & (R[y] < C[k])):
					chrom_baru[y] = chrom[k]

#MENCARI CROSSOVER chromosome
		R = np.random.sample(jum_chromo)
		index_chrom_parent = [] # [1,2,3, ...]
		for p in range(len(R)):
			if(R[p] < self.crossover_rate):
				index_chrom_parent.append(p)
                
#menentukan posisi crossover
		#membangkitkan bilangan acak dengan batasan 1 sampai (panjang chromosome-1), dalam kasus ini bilangan acak yang dibangkitkan adalah 1 – 3.
		posisi_cros = np.random.randint(low=1, high=len(self.gen), size=len(index_chrom_parent))

#menentukan posisi cut-point crossover
		offspring = np.arange(len(self.gen)*len(index_chrom_parent)).reshape(len(index_chrom_parent), len(self.gen))
		for i_parent in range(len(index_chrom_parent)):
			index_chrome_1 = index_chrom_parent[i_parent]
			if(i_parent == len(index_chrom_parent)-1):
				index_chrome_2 = index_chrom_parent[0]
			else:
				index_chrome_2 = index_chrom_parent[i_parent+1]
			#melakukan cut-point
			cut_point = posisi_cros[i_parent]
			for p in range(len(chrom_baru[index_chrome_1])):
				#LOOPING BERDASARKAN GEN
				if(p >= posisi_cros[i_parent]):
					#JIKA GEN[P] LEBIH BESAR ATAU SAMA DENGAN BILANGAN ACAK[P],
					#MAKA DIGANTI DGN CHROMOSOME KE-2
					offspring[i_parent][p] = chrom_baru[index_chrome_2][p]
				else:
					offspring[i_parent][p] = chrom_baru[index_chrome_1][p]

		#PROSES CROSSOVER DISIMPAN PADA VARIABLE 'OFFSPRING'
		#MELAKUKAN PENGGABUNGAN OFFSPRING DENGAN chrom_baru
		for x in range(len(offspring)):
			chrom_baru[index_chrom_parent[x]] = offspring[x]
            
#mutasi chromosome
# Misal ρm kita tentukan 10% maka diharapkan ada 10% dari total_gen yang mengalami populasi:
# jumlah mutasi      = 0.1 * 24
# = 2.4
# = 2

		total_gen = len(chrom) * len(chrom[0])
		jum_mutasi = self.mutasi_rate * total_gen #rumus menghitung jumlah mutasi
		jum_mutasi = int(jum_mutasi)

		random_i_mutasi = np.random.randint(low=0, high=total_gen, size=jum_mutasi)

		for x in range(len(random_i_mutasi)):
			index_mutasi = random_i_mutasi[x]
			byk_kromosom = len(chrom)
			byk_gen = len(chrom[0])
			random_value = random.randint(self.nilai_per_gen['min'], self.nilai_per_gen['max'])
			if(index_mutasi <= byk_gen):
				#jika index_mutasi <= banyak gen, maka akan mengganti
				#gen pada chromosome baru yang ke-0
				chrom_baru[0][index_mutasi-1]
			else:
				#POSISI Y DARI KROMOSOM, UNTUK MENCARI INDEX
				posisi_y = index_mutasi/byk_gen
				posisi_y = int(posisi_y)
				posisi_x = index_mutasi % byk_gen
				chrom_baru[posisi_y][posisi_x] = random_value
		return chrom_baru

	def do_now(self):
		chromosome_current = self.first_chrom
		for generasi in range(0, self.total_gen):
			if(self.stop != True):
				chromosome_current = self.evaluasi_chrom(chromosome_current, generasi)
		print("----------------------------------------------------------------------")
		print("ALL DONE!")
		print("CHROMOSOME TERTINGGI DAN TERBAIK ADALAH")
		print(self.next_gen)

run = Algoritma_genetika()
run.do_now()
      


# In[ ]:





# In[ ]:





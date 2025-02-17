from calendar import monthrange


class timestamp:
	def __init__(self, mo,d,h,m):
		self.mo = mo
		self.d = d
		self.h = h
		self.m = m
	
	def inMinutes(self):
		monthtime = 0
		for i in range(1,self.mo):
			monthtime += monthrange(1518,i)[1]*24*60
		return monthtime + self.d*24*60 + self.h*60 + self.m

def timeDif(time1, time2):


	mod = time1.mo-time2.mo
	dd = time1.d-time2.d
	hd = time1.h-time2.h
	md = time1.m-time2.m

	if mod != 0:
		monthsBetween = mod-1
		dd = monthrange(1518,time1.mo)[1]-time1.d
		dd += time2.d
		for i in range(monthsBetween):
			dd += monthrange(1518, time2.mo+i+1)[1]
	
	if dd != 0:
		daysBetween = dd-1
		hd = 24-time2.h+time1.h
		for i in range(daysBetween):
			hd += 24

	return (hd*60) + md

class Guard:
	def __init__(self,idNum):
		self.idNum = idNum
		self.sleepLog = []
		for i in range(1440):
			self.sleepLog.append(0)
	
	def logSleep(self, dt, length):
		for i in range(dt.inMinutes(), dt.inMinutes()+length):
			if i < 1440:
				self.sleepLog[i] += 1
			
			else:
				while i >= 1440:
					i-= 1440
				
				self.sleepLog[i] += 1

	def totalMinutesSlept(self):
		total = 0
		for i in self.sleepLog:
			total += i
		return total
	
	def minuteMostSlept(self):
		minuteNo = 0
		minutes = 0
		for i in range(len(self.sleepLog)):
			if self.sleepLog[i] > minutes:
				minutes = self.sleepLog[i]
				minuteNo = i
		return [minutes, minuteNo]


	def printInfo(self):
		print("idNum:",self.idNum)

		print("Total:",self.totalMinutesSlept(),"\nMinute most slept:",self.minuteMostSlept()[1],"\nMinutes slept that minute:",self.minuteMostSlept()[0])
		

def guardWithID(idNum, guards):
	for i in guards:
		if i.idNum == idNum:
			return i
	
	return False


def parse(instr):
	logs = []
	addstr = ""
	for i in range(len(instr)):
		if instr[i] == "\n":

			logs.append(addstr)
			addstr = ""

		else:
			addstr = addstr + instr[i]
	logs.append(addstr)
	
	return sorted(logs)


if True:
	test = """[1518-11-01 00:00] Guard #10 begins shift
	[1518-11-01 00:05] falls asleep
	[1518-11-01 00:25] wakes up
	[1518-11-01 00:30] falls asleep
	[1518-11-01 00:55] wakes up
	[1518-11-01 23:58] Guard #99 begins shift
	[1518-11-02 00:40] falls asleep
	[1518-11-02 00:50] wakes up
	[1518-11-03 00:05] Guard #10 begins shift
	[1518-11-03 00:24] falls asleep
	[1518-11-03 00:29] wakes up
	[1518-11-04 00:02] Guard #99 begins shift
	[1518-11-04 00:36] falls asleep
	[1518-11-04 00:46] wakes up
	[1518-11-05 00:03] Guard #99 begins shift
	[1518-11-05 00:45] falls asleep
	[1518-11-05 00:55] wakes up"""

	puzzle = """[1518-05-11 00:22] falls asleep
	[1518-10-11 00:51] wakes up
	[1518-10-12 00:31] wakes up
	[1518-04-08 00:57] wakes up
	[1518-09-26 23:59] Guard #2851 begins shift
	[1518-11-06 00:40] wakes up
	[1518-08-06 00:04] Guard #2851 begins shift
	[1518-09-27 00:54] wakes up
	[1518-07-09 00:00] Guard #2153 begins shift
	[1518-04-11 00:37] falls asleep
	[1518-10-04 00:28] falls asleep
	[1518-05-22 23:59] Guard #2267 begins shift
	[1518-11-02 00:00] Guard #163 begins shift
	[1518-07-03 00:55] wakes up
	[1518-11-11 00:42] wakes up
	[1518-08-06 00:45] falls asleep
	[1518-07-01 00:35] wakes up
	[1518-04-12 00:51] wakes up
	[1518-09-20 00:49] wakes up
	[1518-06-24 00:04] falls asleep
	[1518-07-02 00:54] wakes up
	[1518-06-22 00:43] falls asleep
	[1518-04-01 23:57] Guard #163 begins shift
	[1518-06-02 00:55] falls asleep
	[1518-08-28 00:18] falls asleep
	[1518-05-27 00:10] falls asleep
	[1518-07-31 00:18] falls asleep
	[1518-11-14 00:08] falls asleep
	[1518-06-04 00:58] wakes up
	[1518-10-30 00:59] wakes up
	[1518-04-14 00:48] wakes up
	[1518-10-08 23:56] Guard #1601 begins shift
	[1518-03-08 00:42] falls asleep
	[1518-06-14 00:53] falls asleep
	[1518-11-16 00:31] falls asleep
	[1518-07-09 00:48] wakes up
	[1518-04-29 00:48] wakes up
	[1518-08-30 00:49] wakes up
	[1518-08-26 00:33] falls asleep
	[1518-09-04 00:48] falls asleep
	[1518-07-18 00:46] wakes up
	[1518-03-17 00:53] wakes up
	[1518-08-02 00:46] falls asleep
	[1518-08-13 00:55] wakes up
	[1518-03-15 23:57] Guard #2267 begins shift
	[1518-03-26 23:48] Guard #2851 begins shift
	[1518-11-08 00:05] falls asleep
	[1518-11-22 00:27] wakes up
	[1518-04-19 00:18] wakes up
	[1518-11-09 00:18] falls asleep
	[1518-08-20 00:39] wakes up
	[1518-06-07 00:13] falls asleep
	[1518-10-09 00:34] falls asleep
	[1518-10-15 00:46] wakes up
	[1518-09-01 00:45] falls asleep
	[1518-11-14 00:16] wakes up
	[1518-06-05 00:54] wakes up
	[1518-09-15 00:29] falls asleep
	[1518-07-08 00:20] falls asleep
	[1518-03-09 00:34] wakes up
	[1518-11-07 00:47] wakes up
	[1518-03-27 00:46] falls asleep
	[1518-03-27 00:02] falls asleep
	[1518-05-23 00:21] falls asleep
	[1518-06-19 00:00] Guard #967 begins shift
	[1518-10-09 00:54] falls asleep
	[1518-09-17 00:03] falls asleep
	[1518-11-04 23:46] Guard #2851 begins shift
	[1518-06-29 00:09] falls asleep
	[1518-06-01 00:32] falls asleep
	[1518-05-30 23:56] Guard #1307 begins shift
	[1518-05-12 23:57] Guard #2267 begins shift
	[1518-05-30 00:37] falls asleep
	[1518-04-18 00:57] wakes up
	[1518-04-23 00:27] wakes up
	[1518-03-10 00:36] falls asleep
	[1518-10-21 00:47] falls asleep
	[1518-09-23 23:47] Guard #2399 begins shift
	[1518-05-15 00:06] falls asleep
	[1518-07-14 00:04] falls asleep
	[1518-10-14 00:56] wakes up
	[1518-11-19 00:14] falls asleep
	[1518-05-17 00:19] falls asleep
	[1518-05-26 00:28] falls asleep
	[1518-05-19 00:51] wakes up
	[1518-06-23 00:20] falls asleep
	[1518-04-04 00:45] falls asleep
	[1518-09-21 00:40] falls asleep
	[1518-03-04 00:54] falls asleep
	[1518-07-30 00:30] falls asleep
	[1518-07-02 23:57] Guard #691 begins shift
	[1518-07-29 00:07] wakes up
	[1518-04-29 00:38] falls asleep
	[1518-08-24 00:32] wakes up
	[1518-04-03 00:30] falls asleep
	[1518-06-09 00:54] wakes up
	[1518-07-22 00:27] wakes up
	[1518-09-15 00:56] falls asleep
	[1518-05-24 00:07] wakes up
	[1518-03-24 00:43] wakes up
	[1518-05-24 00:05] falls asleep
	[1518-11-17 00:24] wakes up
	[1518-06-04 00:05] falls asleep
	[1518-08-31 00:56] falls asleep
	[1518-11-19 00:22] wakes up
	[1518-07-12 23:59] Guard #2153 begins shift
	[1518-07-27 00:06] falls asleep
	[1518-05-31 00:35] wakes up
	[1518-06-15 00:40] wakes up
	[1518-08-17 00:57] wakes up
	[1518-10-13 00:07] falls asleep
	[1518-04-22 00:10] falls asleep
	[1518-10-11 00:55] falls asleep
	[1518-09-16 23:51] Guard #2851 begins shift
	[1518-10-21 00:37] falls asleep
	[1518-04-17 00:04] falls asleep
	[1518-06-06 00:00] Guard #2617 begins shift
	[1518-03-04 00:04] Guard #1307 begins shift
	[1518-07-08 00:04] Guard #2399 begins shift
	[1518-04-15 23:56] Guard #2267 begins shift
	[1518-11-04 00:10] falls asleep
	[1518-04-21 23:58] Guard #2851 begins shift
	[1518-07-10 00:52] wakes up
	[1518-09-14 00:57] wakes up
	[1518-09-23 00:34] falls asleep
	[1518-08-02 00:26] falls asleep
	[1518-05-25 00:28] falls asleep
	[1518-07-26 00:56] wakes up
	[1518-03-23 00:03] Guard #509 begins shift
	[1518-05-19 00:44] wakes up
	[1518-07-17 00:02] Guard #691 begins shift
	[1518-06-02 00:57] wakes up
	[1518-10-05 00:48] falls asleep
	[1518-04-04 00:29] wakes up
	[1518-04-28 00:57] wakes up
	[1518-10-22 00:00] Guard #1051 begins shift
	[1518-07-31 23:47] Guard #2447 begins shift
	[1518-05-16 00:45] wakes up
	[1518-08-28 00:52] falls asleep
	[1518-07-17 23:59] Guard #3559 begins shift
	[1518-07-13 00:53] wakes up
	[1518-07-29 00:54] wakes up
	[1518-11-10 00:56] falls asleep
	[1518-11-13 00:33] falls asleep
	[1518-05-15 00:54] wakes up
	[1518-11-01 00:14] falls asleep
	[1518-04-30 00:28] wakes up
	[1518-06-07 00:32] wakes up
	[1518-04-21 00:20] falls asleep
	[1518-04-26 00:31] wakes up
	[1518-11-10 23:59] Guard #1091 begins shift
	[1518-04-27 00:51] wakes up
	[1518-08-27 00:47] wakes up
	[1518-10-12 00:26] falls asleep
	[1518-08-13 00:02] Guard #2153 begins shift
	[1518-03-12 00:59] wakes up
	[1518-08-07 00:20] wakes up
	[1518-03-17 00:28] wakes up
	[1518-11-17 23:59] Guard #1051 begins shift
	[1518-06-26 00:02] falls asleep
	[1518-04-16 23:54] Guard #2267 begins shift
	[1518-11-15 00:59] wakes up
	[1518-08-15 00:01] falls asleep
	[1518-10-22 00:58] wakes up
	[1518-10-24 23:56] Guard #1117 begins shift
	[1518-09-24 00:51] wakes up
	[1518-06-16 00:42] falls asleep
	[1518-03-14 00:51] wakes up
	[1518-03-30 00:18] falls asleep
	[1518-05-01 23:46] Guard #1601 begins shift
	[1518-06-06 00:26] falls asleep
	[1518-04-06 00:51] wakes up
	[1518-10-09 00:57] wakes up
	[1518-07-01 00:43] falls asleep
	[1518-08-31 00:45] wakes up
	[1518-10-07 00:01] Guard #163 begins shift
	[1518-04-17 23:59] Guard #1307 begins shift
	[1518-03-10 00:44] wakes up
	[1518-09-14 00:55] falls asleep
	[1518-09-02 00:47] wakes up
	[1518-08-09 00:13] falls asleep
	[1518-06-06 00:56] wakes up
	[1518-10-10 00:00] Guard #1601 begins shift
	[1518-11-02 00:53] wakes up
	[1518-07-03 00:32] falls asleep
	[1518-10-18 23:59] Guard #1051 begins shift
	[1518-09-07 00:47] wakes up
	[1518-04-25 00:15] falls asleep
	[1518-09-04 00:40] wakes up
	[1518-05-20 00:57] wakes up
	[1518-05-26 00:43] wakes up
	[1518-10-30 00:40] falls asleep
	[1518-08-11 00:54] wakes up
	[1518-11-05 00:59] wakes up
	[1518-07-30 00:17] falls asleep
	[1518-06-09 23:56] Guard #2851 begins shift
	[1518-10-27 00:12] wakes up
	[1518-10-15 23:58] Guard #2267 begins shift
	[1518-05-26 00:51] falls asleep
	[1518-04-15 00:46] wakes up
	[1518-10-27 00:33] falls asleep
	[1518-10-25 00:58] wakes up
	[1518-04-20 00:52] wakes up
	[1518-10-28 23:58] Guard #1307 begins shift
	[1518-10-02 00:17] falls asleep
	[1518-06-25 23:52] Guard #1601 begins shift
	[1518-03-06 00:59] wakes up
	[1518-08-31 00:23] falls asleep
	[1518-09-03 00:04] Guard #1051 begins shift
	[1518-04-03 23:51] Guard #163 begins shift
	[1518-09-29 00:00] Guard #269 begins shift
	[1518-10-07 23:58] Guard #2851 begins shift
	[1518-05-23 00:57] falls asleep
	[1518-09-20 00:24] falls asleep
	[1518-03-28 00:38] wakes up
	[1518-10-26 00:07] falls asleep
	[1518-06-16 00:23] wakes up
	[1518-08-07 00:18] falls asleep
	[1518-09-22 00:00] Guard #509 begins shift
	[1518-11-09 00:00] Guard #3203 begins shift
	[1518-06-08 00:07] falls asleep
	[1518-09-04 23:58] Guard #3559 begins shift
	[1518-05-21 00:55] falls asleep
	[1518-09-21 00:45] wakes up
	[1518-08-13 23:56] Guard #163 begins shift
	[1518-07-02 00:01] Guard #1091 begins shift
	[1518-09-03 00:36] falls asleep
	[1518-05-10 00:06] falls asleep
	[1518-06-16 00:00] Guard #509 begins shift
	[1518-08-18 00:15] wakes up
	[1518-05-08 00:49] falls asleep
	[1518-07-29 00:30] wakes up
	[1518-08-23 00:32] wakes up
	[1518-06-18 00:46] wakes up
	[1518-08-10 00:12] falls asleep
	[1518-10-09 00:51] wakes up
	[1518-03-17 00:41] falls asleep
	[1518-03-17 00:38] wakes up
	[1518-06-20 00:04] Guard #3559 begins shift
	[1518-07-24 00:43] wakes up
	[1518-04-11 00:48] wakes up
	[1518-11-05 00:28] falls asleep
	[1518-04-06 00:24] falls asleep
	[1518-06-09 00:00] Guard #3203 begins shift
	[1518-06-27 00:32] falls asleep
	[1518-08-21 23:56] Guard #2267 begins shift
	[1518-06-03 00:21] falls asleep
	[1518-06-27 00:00] Guard #2617 begins shift
	[1518-05-16 00:28] wakes up
	[1518-11-21 00:44] wakes up
	[1518-03-08 00:36] wakes up
	[1518-04-03 00:00] Guard #2447 begins shift
	[1518-03-17 00:11] wakes up
	[1518-05-19 00:26] falls asleep
	[1518-04-12 00:48] falls asleep
	[1518-10-09 00:38] wakes up
	[1518-03-11 00:40] wakes up
	[1518-05-02 00:39] falls asleep
	[1518-05-28 00:58] wakes up
	[1518-09-30 00:45] falls asleep
	[1518-04-07 00:21] falls asleep
	[1518-06-23 00:22] wakes up
	[1518-04-29 23:56] Guard #349 begins shift
	[1518-03-12 00:01] Guard #1601 begins shift
	[1518-03-28 23:58] Guard #1307 begins shift
	[1518-05-21 00:08] wakes up
	[1518-05-21 00:23] falls asleep
	[1518-08-24 00:01] Guard #2333 begins shift
	[1518-09-01 23:57] Guard #1601 begins shift
	[1518-05-08 00:32] wakes up
	[1518-07-08 00:58] wakes up
	[1518-11-16 00:53] wakes up
	[1518-07-07 00:35] falls asleep
	[1518-06-26 00:22] wakes up
	[1518-09-09 00:48] falls asleep
	[1518-04-05 00:52] falls asleep
	[1518-05-30 00:57] wakes up
	[1518-08-26 00:43] wakes up
	[1518-06-25 00:03] Guard #1307 begins shift
	[1518-07-19 00:02] falls asleep
	[1518-08-01 00:01] falls asleep
	[1518-07-21 23:58] Guard #269 begins shift
	[1518-08-16 00:53] wakes up
	[1518-08-25 00:04] Guard #1307 begins shift
	[1518-06-14 00:28] falls asleep
	[1518-05-09 00:56] falls asleep
	[1518-04-18 23:57] Guard #1051 begins shift
	[1518-04-20 00:15] falls asleep
	[1518-10-10 00:20] falls asleep
	[1518-09-09 00:39] wakes up
	[1518-04-14 00:03] Guard #3203 begins shift
	[1518-03-29 00:54] wakes up
	[1518-07-26 00:49] wakes up
	[1518-11-04 00:01] Guard #2851 begins shift
	[1518-10-26 00:46] wakes up
	[1518-08-13 00:39] falls asleep
	[1518-09-22 00:41] falls asleep
	[1518-04-26 00:24] falls asleep
	[1518-06-15 00:45] falls asleep
	[1518-03-12 00:06] falls asleep
	[1518-03-30 00:00] Guard #353 begins shift
	[1518-10-17 00:33] falls asleep
	[1518-10-03 00:58] wakes up
	[1518-10-08 00:50] wakes up
	[1518-05-24 00:54] wakes up
	[1518-05-12 00:53] wakes up
	[1518-09-18 00:55] falls asleep
	[1518-03-16 00:07] falls asleep
	[1518-09-22 00:51] wakes up
	[1518-06-24 00:19] wakes up
	[1518-05-03 00:34] wakes up
	[1518-10-17 00:21] wakes up
	[1518-06-04 00:13] wakes up
	[1518-07-06 00:03] Guard #1153 begins shift
	[1518-04-11 00:54] falls asleep
	[1518-07-30 00:37] falls asleep
	[1518-07-28 00:50] wakes up
	[1518-04-24 00:00] Guard #3559 begins shift
	[1518-06-23 00:54] wakes up
	[1518-11-19 00:00] Guard #2399 begins shift
	[1518-03-04 00:35] wakes up
	[1518-07-16 00:03] Guard #1091 begins shift
	[1518-09-29 00:38] wakes up
	[1518-10-06 00:51] wakes up
	[1518-09-18 00:59] wakes up
	[1518-04-17 00:59] wakes up
	[1518-06-10 00:29] falls asleep
	[1518-05-28 00:38] wakes up
	[1518-07-20 00:12] falls asleep
	[1518-10-22 23:59] Guard #3559 begins shift
	[1518-10-17 00:13] falls asleep
	[1518-06-11 00:14] wakes up
	[1518-08-29 00:53] wakes up
	[1518-10-29 00:58] wakes up
	[1518-03-07 00:24] wakes up
	[1518-05-12 00:08] falls asleep
	[1518-10-01 00:58] wakes up
	[1518-06-12 00:00] Guard #2333 begins shift
	[1518-04-30 00:17] falls asleep
	[1518-05-14 00:02] Guard #1601 begins shift
	[1518-07-01 00:29] falls asleep
	[1518-07-04 00:03] Guard #269 begins shift
	[1518-07-13 00:56] falls asleep
	[1518-09-24 23:56] Guard #2399 begins shift
	[1518-08-20 00:11] falls asleep
	[1518-10-23 00:36] wakes up
	[1518-09-07 00:59] wakes up
	[1518-05-01 00:30] wakes up
	[1518-11-20 00:46] falls asleep
	[1518-10-14 00:15] falls asleep
	[1518-03-08 23:50] Guard #1051 begins shift
	[1518-07-24 00:52] wakes up
	[1518-08-15 00:55] wakes up
	[1518-03-28 00:17] falls asleep
	[1518-05-10 00:00] Guard #2153 begins shift
	[1518-06-18 00:32] falls asleep
	[1518-05-03 00:47] falls asleep
	[1518-05-05 00:10] falls asleep
	[1518-09-08 00:35] falls asleep
	[1518-08-18 00:54] falls asleep
	[1518-03-10 00:32] wakes up
	[1518-03-12 00:53] falls asleep
	[1518-03-08 00:20] wakes up
	[1518-05-31 00:56] wakes up
	[1518-03-05 00:03] Guard #691 begins shift
	[1518-04-23 00:47] falls asleep
	[1518-04-11 00:57] wakes up
	[1518-10-04 23:56] Guard #2447 begins shift
	[1518-10-11 00:28] falls asleep
	[1518-03-21 00:28] wakes up
	[1518-04-15 00:35] falls asleep
	[1518-08-16 00:38] wakes up
	[1518-08-09 23:56] Guard #1307 begins shift
	[1518-07-13 00:24] falls asleep
	[1518-08-31 23:58] Guard #2447 begins shift
	[1518-08-04 00:00] Guard #1153 begins shift
	[1518-06-13 00:16] falls asleep
	[1518-10-10 00:57] wakes up
	[1518-05-29 00:00] Guard #1051 begins shift
	[1518-07-13 00:44] falls asleep
	[1518-09-14 00:07] falls asleep
	[1518-08-05 00:51] falls asleep
	[1518-07-11 00:58] wakes up
	[1518-10-22 00:43] wakes up
	[1518-04-14 00:59] wakes up
	[1518-06-03 23:50] Guard #2399 begins shift
	[1518-10-22 00:49] falls asleep
	[1518-09-10 00:52] wakes up
	[1518-05-04 00:46] wakes up
	[1518-08-27 00:34] falls asleep
	[1518-05-15 00:31] wakes up
	[1518-09-30 00:55] wakes up
	[1518-08-08 00:49] falls asleep
	[1518-11-17 00:20] falls asleep
	[1518-07-01 00:46] wakes up
	[1518-03-05 00:25] falls asleep
	[1518-11-12 00:03] Guard #353 begins shift
	[1518-09-20 23:59] Guard #2153 begins shift
	[1518-06-21 00:57] wakes up
	[1518-11-22 00:14] falls asleep
	[1518-03-23 00:35] wakes up
	[1518-05-04 00:45] falls asleep
	[1518-07-17 00:44] wakes up
	[1518-09-05 23:52] Guard #1601 begins shift
	[1518-10-04 00:01] Guard #163 begins shift
	[1518-08-17 00:42] wakes up
	[1518-09-12 00:04] Guard #349 begins shift
	[1518-11-20 23:59] Guard #2617 begins shift
	[1518-09-17 00:58] wakes up
	[1518-11-14 00:20] falls asleep
	[1518-09-08 00:29] falls asleep
	[1518-05-18 00:55] wakes up
	[1518-03-31 00:07] falls asleep
	[1518-04-14 00:51] falls asleep
	[1518-11-06 00:59] wakes up
	[1518-03-25 00:31] wakes up
	[1518-05-07 00:01] Guard #163 begins shift
	[1518-11-03 00:52] wakes up
	[1518-05-22 00:33] falls asleep
	[1518-06-18 00:25] wakes up
	[1518-08-02 00:02] falls asleep
	[1518-03-17 00:01] Guard #2267 begins shift
	[1518-03-06 00:53] falls asleep
	[1518-09-22 00:17] falls asleep
	[1518-07-23 23:59] Guard #1307 begins shift
	[1518-08-15 00:18] wakes up
	[1518-08-16 00:13] falls asleep
	[1518-08-17 00:48] falls asleep
	[1518-11-20 00:34] falls asleep
	[1518-05-01 00:03] Guard #1091 begins shift
	[1518-06-13 00:24] wakes up
	[1518-09-03 00:32] wakes up
	[1518-09-06 00:53] wakes up
	[1518-04-20 23:47] Guard #1601 begins shift
	[1518-06-13 23:59] Guard #2267 begins shift
	[1518-03-18 00:04] Guard #2447 begins shift
	[1518-06-22 00:53] wakes up
	[1518-09-09 00:33] wakes up
	[1518-11-02 00:29] falls asleep
	[1518-07-27 00:02] Guard #509 begins shift
	[1518-06-28 00:50] wakes up
	[1518-06-05 00:02] Guard #2333 begins shift
	[1518-05-22 00:23] wakes up
	[1518-10-28 00:01] Guard #2399 begins shift
	[1518-04-03 00:21] wakes up
	[1518-10-31 00:33] falls asleep
	[1518-11-11 00:39] falls asleep
	[1518-04-29 00:00] Guard #1601 begins shift
	[1518-06-01 00:41] falls asleep
	[1518-05-10 00:50] falls asleep
	[1518-08-01 00:43] wakes up
	[1518-11-13 00:25] wakes up
	[1518-08-15 00:39] falls asleep
	[1518-03-09 00:03] falls asleep
	[1518-06-14 23:46] Guard #353 begins shift
	[1518-06-20 00:23] falls asleep
	[1518-10-09 00:41] falls asleep
	[1518-09-18 00:10] falls asleep
	[1518-04-20 00:00] Guard #2447 begins shift
	[1518-05-27 00:15] wakes up
	[1518-04-06 00:58] wakes up
	[1518-07-17 00:13] falls asleep
	[1518-10-20 00:21] falls asleep
	[1518-04-14 23:58] Guard #2851 begins shift
	[1518-03-14 00:03] Guard #2851 begins shift
	[1518-03-07 00:47] wakes up
	[1518-09-22 00:38] wakes up
	[1518-05-03 00:02] Guard #2153 begins shift
	[1518-05-14 00:59] wakes up
	[1518-09-09 00:49] wakes up
	[1518-03-25 00:26] falls asleep
	[1518-10-19 00:49] wakes up
	[1518-05-26 00:53] wakes up
	[1518-05-21 00:49] wakes up
	[1518-06-06 00:44] falls asleep
	[1518-07-01 00:00] Guard #353 begins shift
	[1518-03-31 00:30] wakes up
	[1518-06-21 00:50] wakes up
	[1518-08-22 00:59] wakes up
	[1518-06-30 00:32] falls asleep
	[1518-05-13 00:51] wakes up
	[1518-07-07 00:53] wakes up
	[1518-11-06 00:45] falls asleep
	[1518-08-19 23:56] Guard #2267 begins shift
	[1518-04-23 00:37] falls asleep
	[1518-08-01 00:54] falls asleep
	[1518-05-14 23:59] Guard #1117 begins shift
	[1518-09-11 00:58] wakes up
	[1518-03-18 00:13] falls asleep
	[1518-08-03 00:23] wakes up
	[1518-03-18 00:57] falls asleep
	[1518-07-30 00:34] wakes up
	[1518-07-09 23:50] Guard #353 begins shift
	[1518-06-21 00:01] Guard #2399 begins shift
	[1518-10-04 00:43] wakes up
	[1518-06-25 00:40] falls asleep
	[1518-04-08 00:18] falls asleep
	[1518-10-16 00:25] falls asleep
	[1518-07-19 00:56] wakes up
	[1518-06-06 00:37] wakes up
	[1518-03-18 00:39] wakes up
	[1518-07-30 00:27] wakes up
	[1518-10-07 00:24] falls asleep
	[1518-04-06 00:56] falls asleep
	[1518-08-07 00:00] Guard #3203 begins shift
	[1518-05-02 00:00] falls asleep
	[1518-05-03 00:49] wakes up
	[1518-08-09 00:39] wakes up
	[1518-09-26 00:15] falls asleep
	[1518-09-12 00:41] wakes up
	[1518-11-04 00:57] wakes up
	[1518-09-16 00:03] Guard #2153 begins shift
	[1518-07-06 23:57] Guard #691 begins shift
	[1518-10-28 00:50] wakes up
	[1518-04-08 00:49] wakes up
	[1518-09-15 00:58] wakes up
	[1518-05-10 00:55] wakes up
	[1518-11-23 00:50] wakes up
	[1518-04-21 00:11] wakes up
	[1518-03-18 23:57] Guard #1307 begins shift
	[1518-09-18 00:29] wakes up
	[1518-09-15 00:43] falls asleep
	[1518-09-03 00:22] falls asleep
	[1518-09-25 00:57] wakes up
	[1518-10-02 00:53] wakes up
	[1518-07-26 00:39] falls asleep
	[1518-08-14 00:47] wakes up
	[1518-06-09 00:12] falls asleep
	[1518-09-09 00:02] Guard #163 begins shift
	[1518-10-22 00:24] falls asleep
	[1518-03-19 23:59] Guard #1153 begins shift
	[1518-11-06 23:58] Guard #1117 begins shift
	[1518-11-01 00:02] Guard #1051 begins shift
	[1518-08-10 23:59] Guard #509 begins shift
	[1518-07-07 00:38] wakes up
	[1518-08-18 23:59] Guard #2333 begins shift
	[1518-06-17 00:47] wakes up
	[1518-11-18 00:40] wakes up
	[1518-07-10 00:01] falls asleep
	[1518-03-13 00:15] falls asleep
	[1518-10-16 23:56] Guard #691 begins shift
	[1518-10-15 00:17] falls asleep
	[1518-04-18 00:16] falls asleep
	[1518-03-12 00:16] wakes up
	[1518-03-22 00:56] wakes up
	[1518-03-09 00:55] wakes up
	[1518-03-30 23:58] Guard #2447 begins shift
	[1518-04-04 00:01] falls asleep
	[1518-03-17 00:09] falls asleep
	[1518-06-22 00:00] Guard #1051 begins shift
	[1518-09-28 00:55] wakes up
	[1518-04-28 00:45] falls asleep
	[1518-04-17 00:54] wakes up
	[1518-07-22 00:58] wakes up
	[1518-03-04 00:08] falls asleep
	[1518-07-22 00:45] falls asleep
	[1518-06-16 23:58] Guard #163 begins shift
	[1518-05-19 23:58] Guard #2851 begins shift
	[1518-07-14 00:57] wakes up
	[1518-08-01 00:58] wakes up
	[1518-08-25 00:56] falls asleep
	[1518-07-25 00:50] wakes up
	[1518-06-28 00:36] falls asleep
	[1518-05-18 00:02] Guard #2399 begins shift
	[1518-03-21 00:16] falls asleep
	[1518-04-25 23:59] Guard #3203 begins shift
	[1518-05-12 00:21] wakes up
	[1518-11-05 00:50] falls asleep
	[1518-04-17 00:57] falls asleep
	[1518-11-17 00:01] Guard #163 begins shift
	[1518-04-28 00:00] Guard #269 begins shift
	[1518-03-05 00:47] falls asleep
	[1518-05-05 00:28] wakes up
	[1518-06-20 00:58] wakes up
	[1518-08-28 23:56] Guard #2617 begins shift
	[1518-06-01 00:56] wakes up
	[1518-04-08 23:57] Guard #269 begins shift
	[1518-10-03 00:03] Guard #509 begins shift
	[1518-06-02 00:04] Guard #1307 begins shift
	[1518-04-11 00:00] Guard #2333 begins shift
	[1518-06-23 00:51] falls asleep
	[1518-04-10 00:30] falls asleep
	[1518-08-04 23:53] Guard #2153 begins shift
	[1518-06-10 23:53] Guard #2153 begins shift
	[1518-03-15 00:51] falls asleep
	[1518-10-26 23:51] Guard #353 begins shift
	[1518-05-19 00:48] falls asleep
	[1518-08-23 00:31] falls asleep
	[1518-10-21 00:58] wakes up
	[1518-05-17 00:39] wakes up
	[1518-11-22 00:44] wakes up
	[1518-10-18 00:09] falls asleep
	[1518-09-19 00:00] Guard #1061 begins shift
	[1518-09-06 00:37] falls asleep
	[1518-10-18 00:56] wakes up
	[1518-11-19 00:43] falls asleep
	[1518-05-21 23:58] Guard #2153 begins shift
	[1518-11-18 00:31] wakes up
	[1518-04-19 00:08] falls asleep
	[1518-07-23 00:14] falls asleep
	[1518-06-08 00:56] wakes up
	[1518-04-13 00:56] wakes up
	[1518-06-17 00:40] falls asleep
	[1518-03-07 00:15] falls asleep
	[1518-03-15 00:02] falls asleep
	[1518-03-13 00:00] Guard #2153 begins shift
	[1518-05-27 00:00] Guard #269 begins shift
	[1518-03-16 00:58] wakes up
	[1518-04-16 00:39] wakes up
	[1518-11-07 23:50] Guard #2399 begins shift
	[1518-07-21 00:01] Guard #3559 begins shift
	[1518-07-17 00:57] falls asleep
	[1518-06-12 00:52] falls asleep
	[1518-11-05 00:22] wakes up
	[1518-03-15 00:57] wakes up
	[1518-09-26 00:00] Guard #2399 begins shift
	[1518-07-21 00:38] falls asleep
	[1518-08-11 00:29] falls asleep
	[1518-07-29 23:57] Guard #1051 begins shift
	[1518-04-13 00:44] falls asleep
	[1518-05-28 00:04] Guard #691 begins shift
	[1518-05-20 00:39] falls asleep
	[1518-06-10 00:57] falls asleep
	[1518-05-07 00:54] wakes up
	[1518-03-24 00:21] falls asleep
	[1518-10-31 00:00] Guard #2267 begins shift
	[1518-08-28 00:38] wakes up
	[1518-10-29 00:53] falls asleep
	[1518-04-21 00:01] falls asleep
	[1518-09-12 00:06] falls asleep
	[1518-05-31 00:38] falls asleep
	[1518-06-11 00:48] wakes up
	[1518-06-11 00:03] falls asleep
	[1518-05-02 00:35] wakes up
	[1518-10-05 00:57] wakes up
	[1518-07-20 00:50] wakes up
	[1518-10-31 00:52] wakes up
	[1518-09-09 00:28] falls asleep
	[1518-10-27 00:36] wakes up
	[1518-11-06 00:02] Guard #3559 begins shift
	[1518-08-31 00:00] Guard #1091 begins shift
	[1518-05-29 00:57] wakes up
	[1518-09-06 00:28] wakes up
	[1518-07-24 23:58] Guard #269 begins shift
	[1518-06-04 00:43] falls asleep
	[1518-09-19 23:56] Guard #2399 begins shift
	[1518-08-03 00:41] wakes up
	[1518-07-15 00:09] falls asleep
	[1518-03-04 00:59] wakes up
	[1518-04-02 00:12] falls asleep
	[1518-08-21 00:55] wakes up
	[1518-07-29 00:40] falls asleep
	[1518-05-05 00:07] wakes up
	[1518-04-14 00:15] falls asleep
	[1518-08-08 00:00] Guard #3559 begins shift
	[1518-03-11 00:00] falls asleep
	[1518-06-09 00:18] wakes up
	[1518-09-07 00:46] falls asleep
	[1518-09-01 00:56] falls asleep
	[1518-07-27 23:58] Guard #163 begins shift
	[1518-08-18 00:41] falls asleep
	[1518-08-23 00:49] wakes up
	[1518-06-02 23:57] Guard #2447 begins shift
	[1518-11-02 23:54] Guard #509 begins shift
	[1518-04-13 00:08] falls asleep
	[1518-06-09 00:47] falls asleep
	[1518-04-16 00:07] falls asleep
	[1518-07-18 00:43] falls asleep
	[1518-07-31 00:48] falls asleep
	[1518-10-20 00:49] falls asleep
	[1518-11-23 00:37] wakes up
	[1518-07-19 00:21] wakes up
	[1518-05-11 00:51] wakes up
	[1518-06-12 00:53] wakes up
	[1518-04-02 00:33] wakes up
	[1518-06-10 00:58] wakes up
	[1518-10-20 00:03] Guard #2399 begins shift
	[1518-04-25 00:03] Guard #269 begins shift
	[1518-04-12 00:20] wakes up
	[1518-08-14 00:09] falls asleep
	[1518-06-15 00:56] wakes up
	[1518-11-05 00:43] wakes up
	[1518-03-21 00:03] Guard #2333 begins shift
	[1518-05-18 00:17] falls asleep
	[1518-07-07 00:47] falls asleep
	[1518-07-11 00:53] falls asleep
	[1518-08-16 00:51] falls asleep
	[1518-07-22 00:07] falls asleep
	[1518-04-11 23:58] Guard #509 begins shift
	[1518-10-18 00:01] Guard #2333 begins shift
	[1518-07-31 00:00] Guard #2153 begins shift
	[1518-09-05 00:50] wakes up
	[1518-05-23 00:58] wakes up
	[1518-11-12 00:56] wakes up
	[1518-06-23 23:47] Guard #2447 begins shift
	[1518-11-04 00:30] wakes up
	[1518-07-26 00:04] Guard #691 begins shift
	[1518-09-15 00:00] Guard #163 begins shift
	[1518-05-25 00:32] wakes up
	[1518-09-16 00:55] falls asleep
	[1518-05-26 00:41] falls asleep
	[1518-03-22 00:24] falls asleep
	[1518-11-14 23:58] Guard #1601 begins shift
	[1518-05-21 00:57] wakes up
	[1518-05-22 00:22] falls asleep
	[1518-03-23 00:14] falls asleep
	[1518-04-04 23:59] Guard #2399 begins shift
	[1518-07-16 00:52] wakes up
	[1518-11-22 00:43] falls asleep
	[1518-10-28 00:39] falls asleep
	[1518-05-23 00:53] wakes up
	[1518-09-27 00:19] falls asleep
	[1518-04-23 00:10] falls asleep
	[1518-06-07 23:56] Guard #3559 begins shift
	[1518-11-06 00:22] falls asleep
	[1518-08-17 00:39] falls asleep
	[1518-06-09 00:22] falls asleep
	[1518-11-20 00:58] wakes up
	[1518-03-07 00:00] Guard #2399 begins shift
	[1518-10-25 23:59] Guard #1051 begins shift
	[1518-07-25 00:27] falls asleep
	[1518-06-16 00:15] falls asleep
	[1518-07-31 00:58] wakes up
	[1518-09-10 00:29] falls asleep
	[1518-11-04 00:33] falls asleep
	[1518-07-02 00:46] falls asleep
	[1518-09-07 00:00] Guard #2617 begins shift
	[1518-05-16 00:05] falls asleep
	[1518-10-30 00:00] Guard #3203 begins shift
	[1518-06-30 00:53] wakes up
	[1518-05-31 00:43] wakes up
	[1518-05-26 00:35] wakes up
	[1518-08-24 00:13] falls asleep
	[1518-11-17 00:52] wakes up
	[1518-09-28 00:02] Guard #3559 begins shift
	[1518-08-02 00:43] wakes up
	[1518-08-02 00:56] wakes up
	[1518-06-14 00:57] wakes up
	[1518-06-13 00:47] falls asleep
	[1518-03-08 00:54] wakes up
	[1518-09-14 00:48] wakes up
	[1518-10-05 00:06] falls asleep
	[1518-05-08 00:02] Guard #163 begins shift
	[1518-07-27 00:18] wakes up
	[1518-09-07 00:57] falls asleep
	[1518-11-18 00:39] falls asleep
	[1518-09-03 00:43] wakes up
	[1518-05-13 00:17] falls asleep
	[1518-08-05 00:57] falls asleep
	[1518-05-11 23:56] Guard #1601 begins shift
	[1518-11-17 00:39] wakes up
	[1518-11-21 00:38] falls asleep
	[1518-07-18 23:54] Guard #353 begins shift
	[1518-08-11 23:59] Guard #2617 begins shift
	[1518-05-20 00:12] falls asleep
	[1518-08-31 00:57] wakes up
	[1518-04-05 00:57] wakes up
	[1518-05-31 00:54] falls asleep
	[1518-11-15 00:24] falls asleep
	[1518-05-03 23:58] Guard #1117 begins shift
	[1518-07-24 00:41] falls asleep
	[1518-07-26 00:54] falls asleep
	[1518-08-22 23:57] Guard #353 begins shift
	[1518-07-29 00:00] falls asleep
	[1518-04-15 00:29] wakes up
	[1518-03-19 00:45] falls asleep
	[1518-05-31 00:26] falls asleep
	[1518-08-19 00:16] falls asleep
	[1518-10-24 00:01] Guard #349 begins shift
	[1518-07-22 23:56] Guard #1601 begins shift
	[1518-06-03 00:35] wakes up
	[1518-04-23 00:38] wakes up
	[1518-11-14 00:50] wakes up
	[1518-04-08 00:42] falls asleep
	[1518-10-29 00:46] wakes up
	[1518-10-20 00:51] wakes up
	[1518-03-18 00:59] wakes up
	[1518-03-19 00:55] wakes up
	[1518-04-11 00:33] falls asleep
	[1518-05-07 00:22] falls asleep
	[1518-08-28 00:00] Guard #2399 begins shift
	[1518-04-11 00:34] wakes up
	[1518-04-24 00:48] wakes up
	[1518-03-18 00:28] wakes up
	[1518-09-12 00:34] falls asleep
	[1518-09-15 00:34] wakes up
	[1518-08-18 00:03] Guard #353 begins shift
	[1518-03-13 00:45] wakes up
	[1518-05-20 23:57] Guard #1601 begins shift
	[1518-09-01 00:29] wakes up
	[1518-03-09 23:56] Guard #2267 begins shift
	[1518-11-21 23:58] Guard #509 begins shift
	[1518-04-27 00:03] Guard #2267 begins shift
	[1518-05-10 00:38] wakes up
	[1518-09-17 00:19] wakes up
	[1518-09-30 23:53] Guard #1091 begins shift
	[1518-10-16 00:50] wakes up
	[1518-06-21 00:30] falls asleep
	[1518-10-20 00:28] wakes up
	[1518-05-23 23:46] Guard #691 begins shift
	[1518-08-28 00:53] wakes up
	[1518-10-11 23:57] Guard #2851 begins shift
	[1518-09-23 00:43] wakes up
	[1518-06-26 00:57] wakes up
	[1518-08-03 00:51] wakes up
	[1518-08-30 00:44] falls asleep
	[1518-10-17 00:46] wakes up
	[1518-06-01 00:34] wakes up
	[1518-05-16 00:32] falls asleep
	[1518-08-03 00:21] falls asleep
	[1518-05-15 00:45] falls asleep
	[1518-06-11 00:34] falls asleep
	[1518-11-10 00:58] wakes up
	[1518-07-12 00:02] Guard #1061 begins shift
	[1518-03-28 00:01] Guard #163 begins shift
	[1518-06-17 00:30] wakes up
	[1518-08-12 00:06] falls asleep
	[1518-06-16 00:57] wakes up
	[1518-08-03 00:00] Guard #2399 begins shift
	[1518-05-25 23:59] Guard #1307 begins shift
	[1518-03-25 23:50] Guard #163 begins shift
	[1518-09-06 00:03] falls asleep
	[1518-04-22 23:58] Guard #2153 begins shift
	[1518-03-23 23:57] Guard #1091 begins shift
	[1518-03-22 00:42] falls asleep
	[1518-08-08 23:56] Guard #1601 begins shift
	[1518-06-18 00:00] Guard #2267 begins shift
	[1518-06-18 00:15] falls asleep
	[1518-05-20 00:32] wakes up
	[1518-05-04 23:50] Guard #163 begins shift
	[1518-08-09 00:55] wakes up
	[1518-04-06 23:58] Guard #2399 begins shift
	[1518-04-01 00:05] falls asleep
	[1518-08-05 00:54] wakes up
	[1518-07-13 23:51] Guard #2447 begins shift
	[1518-10-19 00:26] falls asleep
	[1518-07-15 00:35] wakes up
	[1518-07-28 23:51] Guard #1117 begins shift
	[1518-05-24 23:56] Guard #163 begins shift
	[1518-05-28 00:17] falls asleep
	[1518-06-21 00:56] falls asleep
	[1518-04-01 00:41] wakes up
	[1518-03-14 23:50] Guard #1307 begins shift
	[1518-11-23 00:04] Guard #3559 begins shift
	[1518-08-29 00:11] falls asleep
	[1518-07-25 00:57] wakes up
	[1518-03-08 00:35] falls asleep
	[1518-11-13 23:58] Guard #2851 begins shift
	[1518-06-15 00:04] falls asleep
	[1518-06-14 00:47] wakes up
	[1518-07-04 00:37] falls asleep
	[1518-10-13 00:02] Guard #3203 begins shift
	[1518-09-05 00:40] falls asleep
	[1518-11-23 00:31] falls asleep
	[1518-09-23 00:00] Guard #2153 begins shift
	[1518-03-17 00:31] falls asleep
	[1518-11-01 00:43] wakes up
	[1518-03-08 00:02] Guard #2851 begins shift
	[1518-11-09 23:59] Guard #3559 begins shift
	[1518-05-24 00:27] falls asleep
	[1518-07-17 00:59] wakes up
	[1518-08-03 00:47] falls asleep
	[1518-11-17 00:29] falls asleep
	[1518-07-13 00:35] wakes up
	[1518-09-11 00:25] falls asleep
	[1518-09-13 00:42] wakes up
	[1518-07-19 00:31] falls asleep
	[1518-08-23 00:16] falls asleep
	[1518-03-09 00:37] falls asleep
	[1518-04-12 23:57] Guard #1091 begins shift
	[1518-04-23 00:59] wakes up
	[1518-03-05 00:55] wakes up
	[1518-04-03 00:58] wakes up
	[1518-07-24 00:48] falls asleep
	[1518-11-08 00:41] wakes up
	[1518-05-11 00:02] Guard #353 begins shift
	[1518-05-21 00:06] falls asleep
	[1518-08-22 00:57] falls asleep
	[1518-05-05 23:58] Guard #3203 begins shift
	[1518-08-14 23:47] Guard #3203 begins shift
	[1518-05-06 00:27] wakes up
	[1518-06-17 00:25] falls asleep
	[1518-04-27 00:14] falls asleep
	[1518-04-07 00:48] wakes up
	[1518-08-25 23:56] Guard #1091 begins shift
	[1518-07-20 00:42] falls asleep
	[1518-06-28 00:00] Guard #353 begins shift
	[1518-07-05 00:51] falls asleep
	[1518-03-05 23:59] Guard #1307 begins shift
	[1518-10-21 00:38] wakes up
	[1518-09-01 00:57] wakes up
	[1518-05-09 00:00] Guard #1051 begins shift
	[1518-07-23 00:40] wakes up
	[1518-08-12 00:55] wakes up
	[1518-03-27 00:59] wakes up
	[1518-07-20 00:37] wakes up
	[1518-08-18 00:14] falls asleep
	[1518-04-03 00:07] falls asleep
	[1518-09-29 23:59] Guard #1601 begins shift
	[1518-04-04 00:51] wakes up
	[1518-11-13 00:56] wakes up
	[1518-11-12 00:10] falls asleep
	[1518-07-31 00:40] wakes up
	[1518-10-25 00:17] falls asleep
	[1518-08-06 00:55] wakes up
	[1518-05-06 00:08] falls asleep
	[1518-09-17 00:52] falls asleep
	[1518-03-05 00:30] wakes up
	[1518-10-24 00:15] falls asleep
	[1518-06-05 00:06] falls asleep
	[1518-09-01 00:17] falls asleep
	[1518-03-10 23:51] Guard #349 begins shift
	[1518-05-15 23:47] Guard #3203 begins shift
	[1518-11-15 23:59] Guard #691 begins shift
	[1518-10-29 00:34] falls asleep
	[1518-04-25 00:55] wakes up
	[1518-08-23 00:19] wakes up
	[1518-08-30 00:04] Guard #2617 begins shift
	[1518-09-12 23:57] Guard #1051 begins shift
	[1518-07-09 00:36] falls asleep
	[1518-05-17 00:04] Guard #1601 begins shift
	[1518-09-15 00:53] wakes up
	[1518-03-17 00:27] falls asleep
	[1518-06-09 00:42] wakes up
	[1518-07-15 00:04] Guard #269 begins shift
	[1518-05-08 00:27] falls asleep
	[1518-08-21 00:00] Guard #2617 begins shift
	[1518-08-25 00:58] wakes up
	[1518-07-25 00:54] falls asleep
	[1518-11-05 00:01] falls asleep
	[1518-09-26 00:50] wakes up
	[1518-08-27 00:00] Guard #1601 begins shift
	[1518-06-22 23:50] Guard #2447 begins shift
	[1518-09-18 00:02] Guard #691 begins shift
	[1518-04-13 00:38] wakes up
	[1518-09-16 00:57] wakes up
	[1518-06-10 00:32] wakes up
	[1518-08-18 00:56] wakes up
	[1518-05-14 00:26] falls asleep
	[1518-05-29 23:59] Guard #2333 begins shift
	[1518-06-23 00:02] falls asleep
	[1518-11-13 00:22] falls asleep
	[1518-09-15 00:46] wakes up
	[1518-05-28 00:43] falls asleep
	[1518-05-22 00:55] wakes up
	[1518-03-27 00:39] wakes up
	[1518-03-07 00:39] falls asleep
	[1518-08-23 00:46] falls asleep
	[1518-07-05 00:53] wakes up
	[1518-08-05 00:37] wakes up
	[1518-05-19 00:37] falls asleep
	[1518-04-12 00:15] falls asleep
	[1518-10-14 00:00] Guard #1307 begins shift
	[1518-07-16 00:38] falls asleep
	[1518-11-03 00:02] falls asleep
	[1518-11-17 00:44] falls asleep
	[1518-09-08 00:49] wakes up
	[1518-03-08 00:17] falls asleep
	[1518-11-20 00:39] wakes up
	[1518-08-17 00:04] Guard #3203 begins shift
	[1518-03-26 00:03] falls asleep
	[1518-07-04 00:57] wakes up
	[1518-07-28 00:18] falls asleep
	[1518-04-08 00:02] Guard #1051 begins shift
	[1518-06-29 00:03] Guard #269 begins shift
	[1518-03-14 00:07] falls asleep
	[1518-03-25 00:00] Guard #2851 begins shift
	[1518-03-22 00:00] Guard #1117 begins shift
	[1518-09-03 23:59] Guard #691 begins shift
	[1518-05-12 00:40] falls asleep
	[1518-04-22 00:25] wakes up
	[1518-09-12 00:15] wakes up
	[1518-07-29 00:23] falls asleep
	[1518-09-13 00:30] falls asleep
	[1518-11-09 00:56] wakes up
	[1518-10-08 00:22] falls asleep
	[1518-10-07 00:31] wakes up
	[1518-05-18 23:56] Guard #163 begins shift
	[1518-11-19 23:59] Guard #691 begins shift
	[1518-09-08 00:31] wakes up
	[1518-10-01 00:05] falls asleep
	[1518-08-05 00:02] falls asleep
	[1518-10-03 00:22] falls asleep
	[1518-08-02 00:15] wakes up
	[1518-11-23 00:41] falls asleep
	[1518-05-29 00:30] falls asleep
	[1518-06-23 00:15] wakes up
	[1518-03-27 00:09] wakes up
	[1518-07-14 00:28] wakes up
	[1518-06-13 00:59] wakes up
	[1518-09-28 00:42] falls asleep
	[1518-03-29 00:19] falls asleep
	[1518-10-11 00:58] wakes up
	[1518-04-08 00:54] falls asleep
	[1518-03-18 00:37] falls asleep
	[1518-10-24 00:37] wakes up
	[1518-07-19 23:58] Guard #2267 begins shift
	[1518-04-24 00:47] falls asleep
	[1518-03-22 00:32] wakes up
	[1518-07-22 00:55] falls asleep
	[1518-09-14 00:00] Guard #2153 begins shift
	[1518-04-08 00:35] wakes up
	[1518-07-22 00:48] wakes up
	[1518-09-02 00:40] falls asleep
	[1518-11-19 00:51] wakes up
	[1518-09-24 00:04] falls asleep
	[1518-10-02 00:01] Guard #163 begins shift
	[1518-03-16 00:20] wakes up
	[1518-06-26 00:46] falls asleep
	[1518-05-05 00:02] falls asleep
	[1518-05-09 00:59] wakes up
	[1518-03-30 00:37] wakes up
	[1518-06-12 23:57] Guard #353 begins shift
	[1518-09-09 23:59] Guard #353 begins shift
	[1518-11-18 00:17] falls asleep
	[1518-07-05 00:00] Guard #691 begins shift
	[1518-09-29 00:12] falls asleep
	[1518-03-31 23:51] Guard #163 begins shift
	[1518-04-09 00:45] falls asleep
	[1518-07-21 00:47] wakes up
	[1518-07-14 00:53] falls asleep
	[1518-10-13 00:56] wakes up
	[1518-04-09 23:59] Guard #2267 begins shift
	[1518-08-10 00:52] wakes up
	[1518-04-09 00:55] wakes up
	[1518-09-04 00:51] wakes up
	[1518-08-18 00:45] wakes up
	[1518-08-05 00:59] wakes up
	[1518-03-26 00:47] wakes up
	[1518-03-16 00:26] falls asleep
	[1518-04-10 00:57] wakes up
	[1518-04-15 00:21] falls asleep
	[1518-06-22 00:35] falls asleep
	[1518-05-02 00:54] wakes up
	[1518-10-21 00:04] Guard #2267 begins shift
	[1518-08-15 23:56] Guard #353 begins shift
	[1518-09-08 00:00] Guard #349 begins shift
	[1518-10-14 23:56] Guard #2399 begins shift
	[1518-07-30 00:53] wakes up
	[1518-10-06 00:00] Guard #349 begins shift
	[1518-03-15 00:48] wakes up
	[1518-03-27 00:15] falls asleep
	[1518-03-10 00:12] falls asleep
	[1518-06-01 00:02] Guard #3559 begins shift
	[1518-07-11 00:00] Guard #1307 begins shift
	[1518-05-03 00:20] falls asleep
	[1518-11-07 00:29] falls asleep
	[1518-06-22 00:40] wakes up
	[1518-06-29 23:56] Guard #1091 begins shift
	[1518-10-06 00:08] falls asleep
	[1518-04-21 00:57] wakes up
	[1518-11-13 00:00] Guard #509 begins shift
	[1518-05-19 00:31] wakes up
	[1518-05-01 00:09] falls asleep
	[1518-10-11 00:01] Guard #3203 begins shift
	[1518-08-03 00:28] falls asleep
	[1518-08-01 23:50] Guard #349 begins shift
	[1518-04-05 23:59] Guard #1091 begins shift
	[1518-09-09 00:37] falls asleep
	[1518-05-08 00:56] wakes up
	[1518-08-21 00:37] falls asleep
	[1518-10-27 00:05] falls asleep
	[1518-09-25 00:06] falls asleep
	[1518-08-08 00:57] wakes up
	[1518-07-13 00:59] wakes up
	[1518-09-10 23:58] Guard #1307 begins shift
	[1518-06-07 00:04] Guard #1051 begins shift
	[1518-06-27 00:47] wakes up
	[1518-09-04 00:18] falls asleep
	[1518-10-05 00:42] wakes up
	[1518-06-29 00:42] wakes up
	[1518-08-19 00:49] wakes up
	[1518-09-01 00:47] wakes up
	[1518-06-25 00:53] wakes up
	[1518-09-15 00:52] falls asleep
	[1518-08-09 00:47] falls asleep
	[1518-10-23 00:24] falls asleep"""



def readLine(line):
	mo = int(line[6:8])
	d = int(line[9:11])
	h = int(line[12:14])
	m = int(line[15:17])
	sleepLine = False
	if line[19] == "f":
		sleepLine = True

	idNum = None


	if line[19] == "G":
		idNum = ""
		for i in range(len(line)):
			if line[i] == "#":
				digits = 1
				while True:
					if line[i+digits] == " ":
						int(idNum)
						break
					else:
						idNum = idNum + line[i+digits]
						digits += 1



	return [mo,d,h,m,sleepLine,idNum]

currentGuard = None
code = parse(puzzle)
guards = []

sleeping = False
startSleep = None
endSleep = None

for i in code:
	stats = readLine(i)

	if stats[4]:
		startSleep = timestamp(stats[0],stats[1],stats[2],stats[3])
		sleeping = True
	else:
		if sleeping:
			endSleep = timestamp(stats[0],stats[1],stats[2],stats[3])
			sleeping = False
			timeSlept = timeDif(endSleep,startSleep)

			currentGuard.logSleep(startSleep, timeSlept)
	
	if stats[5] != None:
		idNum = stats[5]
		if guardWithID(idNum, guards) == False:
			newGuard = Guard(idNum)
			guards.append(newGuard)
			currentGuard = newGuard
		else:
			currentGuard = guardWithID(idNum, guards)


guradWithHighest = Guard(-1)
for i in guards:
	if i.totalMinutesSlept() > guradWithHighest.totalMinutesSlept():
		guradWithHighest = i

guradWithHighest.printInfo()

print("ID * Minute:",int(guradWithHighest.idNum)*guradWithHighest.minuteMostSlept()[1])

guradWithHighest = Guard(-1)
for i in guards:
	if i.minuteMostSlept()[0] > guradWithHighest.minuteMostSlept()[0]:
		guradWithHighest = i

guradWithHighest.printInfo()

print("ID * Minute:",int(guradWithHighest.idNum) * guradWithHighest.minuteMostSlept()[1])
from mrjob.job import MRJob
from mrjob.step import MRStep
class MRWordCount(MRJob):
    def steps(self):
        return [
            MRStep(mapper=self.mapper_oneitemset,
                   reducer=self.reducer_oneitemset)
                ]
          #  MRStep(]
    def mapper_oneitemset(self, _, line):
        for word in line.split():
                yield(word, 1)
    def reducer_oneitemset(self, word, counts):
        minsupport = 2
        support_count = sum(counts)
        if support_count >= minsupport:  
            yield(word, support_count)

if __name__ == '__main__':
    MRWordCount.run()
    

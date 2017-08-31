#!/usr/bin/python3
# Auto-tuner prototype
# Built for INE5540 robot overlords

flags = [
'-falign-functions',
'-falign-jumps',
'-falign-labels',
'-falign-loops',
'-fauto-inc-dec',
'-fbranch-count-reg',
'-fcaller-saves',
'-fcode-hoisting',
'-fcombine-stack-adjustments',
'-fcompare-elim',
'-fcprop-registers',
'-fcrossjumping',
'-fcse-follow-jumps',
'-fcse-skip-blocks',
'-fdce',
'-fdefer-pop',
'-fdelayed-branch',
'-fdelete-null-pointer-checks',
'-fdevirtualize',
'-fdevirtualize-speculatively',
'-fdse',
'-fexpensive-optimizations',
'-fforward-propagate',
'-fgcse',
'-fgcse-after-reload',
'-fgcse-lm',
'-fguess-branch-probability',
'-fhoist-adjacent-loads',
'-fif-conversion',
'-fif-conversion2',
'-findirect-inlining',
'-finline-functions',
'-finline-functions-called-once',
'-finline-small-functions',
'-fipa-bit-cp',
'-fipa-cp',
'-fipa-cp-clone',
'-fipa-icf',
'-fipa-profile',
'-fipa-pure-const',
'-fipa-ra',
'-fipa-reference',
'-fipa-sra',
'-fipa-vrp',
'-fisolate-erroneous-paths-dereference',
'-flra-remat',
'-fmerge-constants',
'-fmove-loop-invariants',
'-foptimize-sibling-calls',
'-foptimize-strlen',
'-fpartial-inlining',
'-fpeel-loops',
'-fpeephole2',
'-fpredictive-commoning',
'-freorder-blocks',
'-freorder-blocks-algorithm=stc',
'-freorder-blocks-and-partition',
'-freorder-functions',
'-frerun-cse-after-loop',
'-fsched-interblock',
'-fsched-spec',
'-fschedule-insns',
'-fschedule-insns2',
'-fshrink-wrap',
'-fshrink-wrap-separate',
'-fsplit-paths',
'-fsplit-wide-types',
'-fssa-backprop',
'-fssa-phiopt',
'-fstore-merging',
'-fstrict-aliasing',
'-fthread-jumps',
'-ftree-bit-ccp',
'-ftree-builtin-call-dce',
'-ftree-ccp',
'-ftree-ch',
'-ftree-coalesce-vars',
'-ftree-copy-prop',
'-ftree-dce',
'-ftree-dominator-opts',
'-ftree-dse',
'-ftree-forwprop',
'-ftree-fre',
'-ftree-loop-distribute-patterns',
'-ftree-loop-distribution',
'-ftree-loop-vectorize',
'-ftree-partial-pre',
'-ftree-phiprop',
'-ftree-pre',
'-ftree-pta',
'-ftree-sink',
'-ftree-slp-vectorize',
'-ftree-slsr',
'-ftree-sra',
'-ftree-switch-conversion',
'-ftree-tail-merge',
'-ftree-ter',
'-ftree-vrp',
'-funit-at-a-time',
'-funswitch-loops',
'-fvect-cost-model',
]

import subprocess # to run stuff
import sys # for args, in case you want them
import time # for time
import math
from itertools import chain, combinations

def tuner(step, fl):
    exec_file = 'matmult'
    compilation_line = ['gcc','-o',exec_file,'mm.c']
    steps = ['-DSTEP='+str(step)]

    # Compile code
    compilation_try = subprocess.run(compilation_line+steps+fl)
    if (compilation_try.returncode == 0):
        print("Happy compilation")
    else:
        print("Sad compilation")

    # Run code
    input_size = str(4)
    t_begin = time.time() # timed run
    run_trial = subprocess.run(['./'+exec_file, input_size])
    t_end = time.time()
    if (run_trial.returncode == 0):
        print("Happy execution in "+str(t_end-t_begin))
        return t_end-t_begin
    else:
        print("Sad execution")
        return 20.0


if __name__ == "__main__":
    
    timer = 20.0
    step_i = 0;
    for i in range(1,10):
        time_i = 20.0
        for a in range(5):
            time_a = tuner(2**i, [])
            if time_a < time_i:
                time_i = time_a
        if  timer > time_i:
            timer = time_i
            step_i = i

    
    bfl = []
    for fl in chain.from_iterable(combinations(flags, r) for r in range(int(sys.argv[1])+1)):
        time_i = 20.0
        for a in range(5):
            time_a = tuner(2**step_i, list(fl))
            if time_a < time_i:
                time_i = time_a
        if  timer > time_i:
            timer = time_i
            bfl = fl

    print("Best STEP="+str(step_i))
    print(bfl)
    print("time = "+str(timer))

 


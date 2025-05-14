# main script
# set up
from utils.scrap import scrap_google

# collect url and locator from all websites
# manually update url and locator if the website changes/add new website

BAMS_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRshH4QuzsOR3f9RtwAaC8yfk-WYiSynZ4FXMdy07UJcl1mRxDIAc26r8Pafydld1dQqNENo7rc93v0/pubhtml?gid=1189407793"
BAMS = scrap_google(BAMS_url)

print(BAMS.head())
print(BAMS.columns)

BQSE_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vR3J_S9rJVlljcVhC1IcG1IY-TkSl75PQAu8jZX9nnfZMx3Jceddn2wOa5WfE-hP5jpbwU_YbpY40Dx/pubhtml?gid=572234617"
BQSE = scrap_google(BQSE_url)
print(BQSE.head())
print(BQSE.columns)
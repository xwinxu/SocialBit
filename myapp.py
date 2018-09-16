#from pprint import pprint
#from fbrecog import recognize
# changed the init file into fbrecogg
from fbrecogg import FBRecog
path = 'testt.png' # Insert your image file path here
#path2 = '2.jpg' # Insert your image ddfile path here
access_token = 'EAATsaLF1VZAMBACKDGBxKZAVUNxnTMrTk0wbWtq1HL5BZALuKbpxgnXyoeEZADZCVj26NXruz7V2CCdcOC2iF6tnKPWsARxKTttfhfilm1ZBtY5eq9lo2mvRxnhMCEs9caoq3k9q3UZAf2qtejqB2aB2a7EYIIwgEfTvVYRT3R7hZAj1jWa8ZCX3ZB3i3JPIBqjrnl2aaowOQIcIRQZBNMaLKtcdBQCFFt3S2e4JJaDGfw0IgZDZD'
cookies = 'datr=O_EsW1YcsATGZhZT7jNF35uQ; sb=Q_EsW1R7eCNVp1ecIAiGni3i; c_user=100001231616532; xs=4%3Ah17Ta3gjazupTA%3A2%3A1529672003%3A7879%3A14888; pl=y; dpr=2; ; spin=r.4317531_b.trunk_t.1537032671_s.1_v.2_; fr=0lNU2EuMhbPwb9JoK.AWWS42OvDItyhJDOc1L-fsS8O6s.BbLCsL.lH.FuV.0.0.BbnWeW.AWXbmkOm; act=1537043229078%2F2; wd=1196x451; presence=EDvF3EtimeF1537043859EuserFA21B01231616532A2EstateFDsb2F1537040045169EatF1537042866368Et3F_5b_5dEutc3F1537040686268G537043859574CEchFDp_5f1B01231616532F745CC'
fb_dtsg = 'AQFlHUWA7L6w:AQF1QEpSzcdT' # Insert the fb_dtsg parameter obtained from Form Data here.
# Instantiate the recog class
recog = FBRecog(access_token, cookies, fb_dtsg)
# Recog class can be used multiple times with different paths
print(recog.recognize(path))
#print(recog.recognize(path2))

# Call recognize_raw to get more info about the faces detected, including their positions
#pprint(recog.recognize_raw(path), indent=2)

def demonstratif(mot):
	analyse=[[],[],[]]
	trad=""
	if mot=="hic":
		trad="celui-ci,celle-ci,ceux-ci"
		analyse[0].append("NOMINATIF SG")
		analyse[0].append("VOCATIF SG")
	elif mot=="hunc":
		trad="celui-ci,celle-ci,ceux-ci"
		analyse[0].append("ACCUSATIF SG")
	elif mot=="huius":
		trad="celui-ci,celle-ci,ceux-ci"
		analyse[0].append("GENITIF SG")
		analyse[1].append("GENITIF SG")
		analyse[2].append("GENITIF SG")
	elif mot=="huic":
		trad="celui-ci,celle-ci,ceux-ci"
		analyse[0].append("DATIF SG")
		analyse[1].append("DATIF SG")
		analyse[2].append("DATIF SG")
	elif mot=="hoc":
		trad="celui-ci,celle-ci,ceux-ci"
		analyse[0].append("ABLATIF SG")
		analyse[2].append("ABLATIF SG")
		analyse[2].append("NOMINATIF SG")
		analyse[2].append("VOCATIF SG")
		analyse[2].append("ACCUSATIF SG")
	elif mot=="haec":
		trad="celui-ci,celle-ci,ceux-ci"
		analyse[1].append("NOMINATIF SG")
		analyse[1].append("VOCATIF SG")
		analyse[2].append("NOMINATIF PL")
		analyse[2].append("VOCATIF PL")
		analyse[2].append("ACCUSATIF PL")
	elif mot=="hac":
		trad="celui-ci,celle-ci,ceux-ci"
		analyse[1].append("ABLATIF SG")
	elif mot=="hi":
		trad="celui-ci,celle-ci,ceux-ci"
		analyse[0].append("NOMINATIF PL")
		analyse[0].append("VOCATIF PL")
	elif mot=="hos":
		trad="celui-ci,celle-ci,ceux-ci"
		analyse[0].append("ACCUSATIF PL")
	elif mot=="horum":
		trad="celui-ci,celle-ci,ceux-ci"
		analyse[0].append("GENITIF PL")
		analyse[2].append("GENITIF PL")
	elif mot=="his":
		trad="celui-ci,celle-ci,ceux-ci"
		analyse[1].append("DATIF PL")
		analyse[1].append("ABLATIF PL")
		analyse[2].append("DATIF PL")
		analyse[2].append("ABLATIF PL")
		analyse[0].append("DATIF PL")
		analyse[0].append("ABLATIF PL")
	elif mot=="hae":
		trad="celui-ci,celle-ci,ceux-ci"
		analyse[1].append("NOMINATIF PL")
		analyse[1].append("VOCATIF PL")
	elif mot=="has":
		trad="celui-ci,celle-ci,ceux-ci"
		analyse[1].append("ACCUSATIF PL")
	elif mot=="harum":
		trad="celui-ci,celle-ci,ceux-ci"
		analyse[1].append("GENITIF PL")
	elif mot=="hanc":
		trad="celui-ci,celle-ci,ceux-ci"
		analyse[1].append("ACCUSATIF SG")


	if mot=="iste":
		trad="celui-l??, celle-l??, ceux-l??"
		analyse[0].append("NOMINATIF SG")
		analyse[0].append("VOCATIF SG")
	elif mot=="istum":
		trad="celui-l??, celle-l??, ceux-l??"
		analyse[0].append("ACCUSATIF SG")
	elif mot=="istius":
		trad="celui-l??, celle-l??, ceux-l??"
		analyse[0].append("GENITIF SG")
		analyse[1].append("GENITIF SG")
		analyse[2].append("GENITIF SG")
	elif mot=="isti":
		trad="celui-l??, celle-l??, ceux-l??"
		analyse[0].append("DATIF SG")
		analyse[1].append("DATIF SG")
		analyse[2].append("DATIF SG")
		analyse[0].append("NOMINATIF PL")
		analyse[0].append("VOCATIF PL")
	elif mot=="isto":
		trad="celui-l??, celle-l??, ceux-l??"
		analyse[0].append("ABLATIF SG")
		analyse[2].append("ABLATIF SG")
	elif mot=="istud":
		trad="celui-l??, celle-l??, ceux-l??"
		analyse[2].append("NOMINATIF SG")
		analyse[2].append("VOCATIF SG")
		analyse[2].append("ACCUSATIF SG")
	elif mot=="ista":
		trad="celui-l??, celle-l??, ceux-l??"
		analyse[1].append("NOMINATIF SG")
		analyse[1].append("VOCATIF SG")
		analyse[2].append("NOMINATIF PL")
		analyse[2].append("VOCATIF PL")
		analyse[2].append("ACCUSATIF PL")
		analyse[1].append("ABLATIF SG")
	elif mot=="istos":
		trad="celui-l??, celle-l??, ceux-l??"
		analyse[0].append("ACCUSATIF PL")
	elif mot=="ostorum":
		trad="celui-l??, celle-l??, ceux-l??"
		analyse[0].append("GENITIF PL")
		analyse[2].append("GENITIF PL")
	elif mot=="istis":
		trad="celui-l??, celle-l??, ceux-l??"
		analyse[1].append("DATIF PL")
		analyse[1].append("ABLATIF PL")
		analyse[2].append("DATIF PL")
		analyse[2].append("ABLATIF PL")
		analyse[0].append("DATIF PL")
		analyse[0].append("ABLATIF PL")
	elif mot=="istae":
		trad="celui-l??, celle-l??, ceux-l??"
		analyse[1].append("NOMINATIF PL")
		analyse[1].append("VOCATIF PL")
	elif mot=="istas":
		trad="celui-l??, celle-l??, ceux-l??"
		analyse[1].append("ACCUSATIF PL")
	elif mot=="istarum":
		trad="celui-l??, celle-l??, ceux-l??"
		analyse[1].append("GENITIF PL")
	elif mot=="istam":
		trad="celui-l??, celle-l??, ceux-l??"
		analyse[1].append("ACCUSATIF SG")


	if mot=="ille":
		trad="celui-l??,celle-l??,ceux-l??"
		analyse[0].append("NOMINATIF SG")
		analyse[0].append("VOCATIF SG")
	elif mot=="illum":
		trad="celui-l??,celle-l??,ceux-l??"
		analyse[0].append("ACCUSATIF SG")
	elif mot=="illius":
		trad="celui-l??,celle-l??,ceux-l??"
		analyse[0].append("GENITIF SG")
		analyse[1].append("GENITIF SG")
		analyse[2].append("GENITIF SG")
	elif mot=="illi":
		trad="celui-l??,celle-l??,ceux-l??"
		analyse[0].append("DATIF SG")
		analyse[1].append("DATIF SG")
		analyse[2].append("DATIF SG")
		analyse[0].append("NOMINATIF PL")
		analyse[0].append("VOCATIF PL")
	elif mot=="illo":
		trad="celui-l??,celle-l??,ceux-l??"
		analyse[0].append("ABLATIF SG")
		analyse[2].append("ABLATIF SG")
	elif mot=="illud":
		trad="celui-l??, celle-l??, ceux-l??"
		analyse[2].append("NOMINATIF SG")
		analyse[2].append("VOCATIF SG")
		analyse[2].append("ACCUSATIF SG")
	elif mot=="illa":
		trad="celui-l??,celle-l??,ceux-l??"
		analyse[1].append("NOMINATIF SG")
		analyse[1].append("VOCATIF SG")
		analyse[2].append("NOMINATIF PL")
		analyse[2].append("VOCATIF PL")
		analyse[2].append("ACCUSATIF PL")
		analyse[1].append("ABLATIF SG")
	elif mot=="illos":
		trad="celui-l??,celle-l??,ceux-l??"
		analyse[0].append("ACCUSATIF PL")
	elif mot=="illorum":
		trad="celui-l??,celle-l??,ceux-l??"
		analyse[0].append("GENITIF PL")
		analyse[2].append("GENITIF PL")
	elif mot=="illis":
		trad="celui-l??,celle-l??,ceux-l??"
		analyse[1].append("DATIF PL")
		analyse[1].append("ABLATIF PL")
		analyse[2].append("DATIF PL")
		analyse[2].append("ABLATIF PL")
		analyse[0].append("DATIF PL")
		analyse[0].append("ABLATIF PL")
	elif mot=="illae":
		trad="celui-l??,celle-l??,ceux-l??"
		analyse[1].append("NOMINATIF PL")
		analyse[1].append("VOCATIF PL")
	elif mot=="illas":
		trad="celui-l??,celle-l??,ceux-l??"
		analyse[1].append("ACCUSATIF PL")
	elif mot=="illarum":
		trad="celui-l??,celle-l??,ceux-l??"
		analyse[1].append("GENITIF PL")
	elif mot=="illam":
		trad="celui-l??, celle-l??, ceux-l??"
		analyse[1].append("ACCUSATIF SG")
	

	if mot=="is":
		trad="ce,cette,cet"
		analyse[0].append("NOMINATIF SG")
		analyse[0].append("VOCATIF SG")
	elif mot=="eum":
		trad="ce,cette,cet"
		analyse[0].append("ACCUSATIF SG")
	elif mot=="eius":
		trad="ce,cette,cet"
		analyse[0].append("GENITIF SG")
		analyse[1].append("GENITIF SG")
		analyse[2].append("GENITIF SG")
	elif mot=="ei":
		trad="ce,cette,cet"
		analyse[0].append("DATIF SG")
		analyse[1].append("DATIF SG")
		analyse[2].append("DATIF SG")
		analyse[0].append("NOMINATIF PL")
		analyse[0].append("VOCATIF PL")
	elif mot=="eo":
		trad="ce,cette,cet"
		analyse[0].append("ABLATIF SG")
		analyse[2].append("ABLATIF SG")
	elif trad=="id":
		trad="ce,cette,cet"
		analyse[2].append("NOMINATIF SG")
		analyse[2].append("VOCATIF SG")
		analyse[2].append("ACCUSATIF SG")
	elif mot=="ea":
		trad="ce,cette,cet"
		analyse[1].append("NOMINATIF SG")
		analyse[1].append("VOCATIF SG")
		analyse[2].append("NOMINATIF PL")
		analyse[2].append("VOCATIF PL")
		analyse[2].append("ACCUSATIF PL")
		analyse[1].append("ABLATIF SG")
	elif mot=="ii":
		trad="ce,cette,cet"
		analyse[0].append("NOMINATIF PL")
		analyse[0].append("VOCATIF PL")
	elif mot=="eos":
		trad="ce,cette,cet"
		analyse[0].append("ACCUSATIF PL")
	elif mot=="eorum":
		trad="ce,cette,cet"
		analyse[0].append("GENITIF PL")
		analyse[2].append("GENITIF PL")
	elif mot=="iis" or mot=="eis":
		trad="ce,cette,cet"
		analyse[1].append("DATIF PL")
		analyse[1].append("ABLATIF PL")
		analyse[2].append("DATIF PL")
		analyse[2].append("ABLATIF PL")
		analyse[0].append("DATIF PL")
		analyse[0].append("ABLATIF PL")
	elif mot=="eae":
		trad="ce,cette,cet"
		analyse[1].append("NOMINATIF PL")
		analyse[1].append("VOCATIF PL")
	elif mot=="eas":
		trad="ce,cette,cet"
		analyse[1].append("ACCUSATIF PL")
	elif mot=="earum":
		trad="ce,cette,cet"
		analyse[1].append("GENITIF PL")
	elif mot=="eam":
		trad="ce,cette,cet"
		analyse[1].append("ACCUSATIF SG")
	

	if mot=="ipse":
		trad="lui-m??me,elle-m??me"
		analyse[0].append("NOMINATIF SG")
		analyse[0].append("VOCATIF SG")
	elif mot=="ipsum":
		trad="lui-m??me,elle-m??me"
		analyse[0].append("ACCUSATIF SG")
		analyse[2].append("NOMINATIF SG")
		analyse[2].append("VOCATIF SG")
		analyse[2].append("ACCUSATIF SG")
	elif mot=="ipsius":
		trad="lui-m??me,elle-m??me"
		analyse[0].append("GENITIF SG")
		analyse[1].append("GENITIF SG")
		analyse[2].append("GENITIF SG")
	elif mot=="ipsi":
		trad="lui-m??me,elle-m??me"
		analyse[0].append("DATIF SG")
		analyse[1].append("DATIF SG")
		analyse[2].append("DATIF SG")
		analyse[0].append("NOMINATIF PL")
		analyse[0].append("VOCATIF PL")
	elif mot=="ipso":
		trad="lui-m??me,elle-m??me"
		analyse[0].append("ABLATIF SG")
		analyse[2].append("ABLATIF SG")
	elif mot=="ipsa":
		trad="lui-m??me,elle-m??me"
		analyse[1].append("NOMINATIF SG")
		analyse[1].append("VOCATIF SG")
		analyse[2].append("NOMINATIF PL")
		analyse[2].append("VOCATIF PL")
		analyse[2].append("ACCUSATIF PL")
		analyse[1].append("ABLATIF SG")
	elif mot=="ipsos":
		trad="lui-m??me,elle-m??me"
		analyse[0].append("ACCUSATIF PL")
	elif mot=="ipsorum":
		trad="lui-m??me,elle-m??me"
		analyse[0].append("GENITIF PL")
		analyse[2].append("GENITIF PL")
	elif mot=="ipsis":
		trad="lui-m??me,elle-m??me"
		analyse[1].append("DATIF PL")
		analyse[1].append("ABLATIF PL")
		analyse[2].append("DATIF PL")
		analyse[2].append("ABLATIF PL")
		analyse[0].append("DATIF PL")
		analyse[0].append("ABLATIF PL")
	elif mot=="ipsae":
		trad="lui-m??me,elle-m??me"
		analyse[1].append("NOMINATIF PL")
		analyse[1].append("VOCATIF PL")
	elif mot=="ipsas":
		trad="lui-m??me,elle-m??me"
		analyse[1].append("ACCUSATIF PL")
	elif mot=="ipsarum":
		trad="lui-m??me,elle-m??me"
		analyse[1].append("GENITIF PL")
	elif mot=="ipsam":
		trad="lui-m??me,elle-m??me"
		analyse[1].append("ACCUSATIF SG")
	


	if mot=="idem":
		trad="le m??me,la m??me"
		analyse[0].append("NOMINATIF SG")
		analyse[0].append("VOCATIF SG")
		analyse[2].append("NOMINATIF SG")
		analyse[2].append("VOCATIF SG")
		analyse[2].append("ACCUSATIF SG")
	elif mot=="eiudem":
		trad="le m??me,la m??me"
		analyse[0].append("ACCUSATIF SG")
	elif mot=="eiusdem":
		trad="le m??me,la m??me"
		analyse[0].append("GENITIF SG")
		analyse[1].append("GENITIF SG")
		analyse[2].append("GENITIF SG")
	elif mot=="eidem":
		trad="le m??me,la m??me"
		analyse[0].append("DATIF SG")
		analyse[1].append("DATIF SG")
		analyse[2].append("DATIF SG")
		analyse[0].append("NOMINATIF PL")
		analyse[0].append("VOCATIF PL")
	elif mot=="eodem":
		trad="le m??me,la m??me"
		analyse[0].append("ABLATIF SG")
		analyse[2].append("ABLATIF SG")
	elif mot=="eadem":
		trad="le m??me,la m??me"
		analyse[1].append("NOMINATIF SG")
		analyse[1].append("VOCATIF SG")
		analyse[2].append("NOMINATIF PL")
		analyse[2].append("VOCATIF PL")
		analyse[2].append("ACCUSATIF PL")
		analyse[1].append("ABLATIF SG")
	elif mot=="iidem":
		trad="le m??me,la m??me"
		analyse[0].append("NOMINATIF PL")
		analyse[0].append("VOCATIF PL")
	elif mot=="eosdem":
		trad="le m??me,la m??me"
		analyse[0].append("ACCUSATIF PL")
	elif mot=="eorundem":
		trad="le m??me,la m??me"
		analyse[0].append("GENITIF PL")
		analyse[2].append("GENITIF PL")
	elif mot=="iisdem" or mot=="eisdem":
		trad="le m??me,la m??me"
		analyse[1].append("DATIF PL")
		analyse[1].append("ABLATIF PL")
		analyse[2].append("DATIF PL")
		analyse[2].append("ABLATIF PL")
		analyse[0].append("DATIF PL")
		analyse[0].append("ABLATIF PL")
	elif mot=="eaedem":
		trad="le m??me,la m??me"
		analyse[1].append("NOMINATIF PL")
		analyse[1].append("VOCATIF PL")
	elif mot=="easdem":
		trad="le m??me,la m??me"
		analyse[1].append("ACCUSATIF PL")
	elif mot=="earundem":
		trad="le m??me,la m??me"
		analyse[1].append("GENITIF PL")
	elif mot=="eandem":
		trad="le m??me,la m??me"
		analyse[1].append("ACCUSATIF SG")
	if trad=="" and analyse==[[],[],[]]:
		return None
	else:
		return [trad,analyse]
def BAGMSGS(year):
    create = """CREATE TABLE [dbo].[OSUSR_UUK_BAGMSGS""" + year + """](
	[ID] [int] NOT NULL,
	[SMI] [nvarchar](3) NULL,
	[SLMI] [nvarchar](3) NULL,
	[STATUSINDICATOR] [nvarchar](3) NULL,
	[BIRREG] [nvarchar](3) NULL,
	[CCORP] [nvarchar](21) NULL,
	[DREMOTELOC] [nvarchar](4) NULL,
	[EEXCEP] [nvarchar](4) NULL,
	[FFLTNR] [nvarchar](8) NULL,
	[FDATE] [datetime] NULL,
	[FDEST] [nvarchar](3) NULL,
	[FCLASS] [nvarchar](1) NULL,
	[HHANDTERM] [nvarchar](6) NULL,
	[HHANDBAY] [nvarchar](6) NULL,
	[HHANDSTDGTE] [nvarchar](16) NULL,
	[IFLTNR] [nvarchar](8) NULL,
	[IDATE] [datetime] NULL,
	[IORIGIN] [nvarchar](3) NULL,
	[ICLASS] [nvarchar](1) NULL,
	[JRECO] [nvarchar](1) NULL,
	[JAGENTID] [nvarchar](9) NULL,
	[JSCANID] [nvarchar](8) NULL,
	[JREADLOC] [nvarchar](8) NULL,
	[JSENTLOC] [nvarchar](8) NULL,
	[KDMP] [nvarchar](11) NULL,
	[LPNR] [nvarchar](10) NULL,
	[NBAGTAG] [nvarchar](13) NULL,
	[NNRTAGS] [nvarchar](3) NULL,
	[OFLTNR] [nvarchar](8) NULL,
	[ODATE] [datetime] NULL,
	[ODEST] [nvarchar](3) NULL,
	[OCLASS] [nvarchar](1) NULL,
	[PPAXNAME] [nvarchar](64) NULL,
	[RINTERNAL] [nvarchar](64) NULL,
	[SAUTL] [nvarchar](1) NULL,
	[SSEAT] [nvarchar](3) NULL,
	[SPAXCK] [nvarchar](1) NULL,
	[SPAXPROF] [nvarchar](1) NULL,
	[SAUTTRANS] [nvarchar](1) NULL,
	[SBAGTAGSTATUS] [nvarchar](1) NULL,
	[TTAGPRINTERID] [nvarchar](12) NULL,
	[UULD] [nvarchar](11) NULL,
	[UCOMPT] [nvarchar](5) NULL,
	[UTYPEOFBAG] [nvarchar](1) NULL,
	[UDESTCONTAINER] [nvarchar](3) NULL,
	[UCONTTYPE] [nvarchar](8) NULL,
	[VBAGSOURCIND] [nvarchar](1) NULL,
	[VCITY] [nvarchar](3) NULL,
	[WPWINDICATOR] [nvarchar](1) NULL,
	[WNRCKBAGS] [nvarchar](50) NULL,
	[WTOTK] [int] NULL,
	[XSECURITY] [nvarchar](63) NULL,
	[YFQTV] [nvarchar](55) NULL,
	[TIMESTAMP] [datetime] NULL,
 CONSTRAINT [OSPRK_OSUSR_UUK_BAGMSGS""" + year + """] PRIMARY KEY CLUSTERED 
(
	[ID]
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]

ALTER TABLE [dbo].[OSUSR_UUK_BAGMSGS""" + year + """] ADD  DEFAULT ('') FOR [SMI]
ALTER TABLE [dbo].[OSUSR_UUK_BAGMSGS""" + year + """] ADD  DEFAULT ('') FOR [SLMI]
ALTER TABLE [dbo].[OSUSR_UUK_BAGMSGS""" + year + """] ADD  DEFAULT ('') FOR [STATUSINDICATOR]
ALTER TABLE [dbo].[OSUSR_UUK_BAGMSGS""" + year + """] ADD  DEFAULT ('') FOR [BIRREG]
ALTER TABLE [dbo].[OSUSR_UUK_BAGMSGS""" + year + """] ADD  DEFAULT ('') FOR [CCORP]
ALTER TABLE [dbo].[OSUSR_UUK_BAGMSGS""" + year + """] ADD  DEFAULT ('') FOR [DREMOTELOC]
ALTER TABLE [dbo].[OSUSR_UUK_BAGMSGS""" + year + """] ADD  DEFAULT ('') FOR [EEXCEP]
ALTER TABLE [dbo].[OSUSR_UUK_BAGMSGS""" + year + """] ADD  DEFAULT ('') FOR [FFLTNR]
ALTER TABLE [dbo].[OSUSR_UUK_BAGMSGS""" + year + """] ADD  DEFAULT ('1900-01-01 00:00:00') FOR [FDATE]
ALTER TABLE [dbo].[OSUSR_UUK_BAGMSGS""" + year + """] ADD  DEFAULT ('') FOR [FDEST]
ALTER TABLE [dbo].[OSUSR_UUK_BAGMSGS""" + year + """] ADD  DEFAULT ('') FOR [FCLASS]
ALTER TABLE [dbo].[OSUSR_UUK_BAGMSGS""" + year + """] ADD  DEFAULT ('') FOR [HHANDTERM]
ALTER TABLE [dbo].[OSUSR_UUK_BAGMSGS""" + year + """] ADD  DEFAULT ('') FOR [HHANDBAY]
ALTER TABLE [dbo].[OSUSR_UUK_BAGMSGS""" + year + """] ADD  DEFAULT ('') FOR [HHANDSTDGTE]
ALTER TABLE [dbo].[OSUSR_UUK_BAGMSGS""" + year + """] ADD  DEFAULT ('') FOR [IFLTNR]
ALTER TABLE [dbo].[OSUSR_UUK_BAGMSGS""" + year + """] ADD  DEFAULT ('1900-01-01 00:00:00') FOR [IDATE]
ALTER TABLE [dbo].[OSUSR_UUK_BAGMSGS""" + year + """] ADD  DEFAULT ('') FOR [IORIGIN]
ALTER TABLE [dbo].[OSUSR_UUK_BAGMSGS""" + year + """] ADD  DEFAULT ('') FOR [ICLASS]
ALTER TABLE [dbo].[OSUSR_UUK_BAGMSGS""" + year + """] ADD  DEFAULT ('') FOR [JRECO]
ALTER TABLE [dbo].[OSUSR_UUK_BAGMSGS""" + year + """] ADD  DEFAULT ('') FOR [JAGENTID]
ALTER TABLE [dbo].[OSUSR_UUK_BAGMSGS""" + year + """] ADD  DEFAULT ('') FOR [JSCANID]
ALTER TABLE [dbo].[OSUSR_UUK_BAGMSGS""" + year + """] ADD  DEFAULT ('') FOR [JREADLOC]
ALTER TABLE [dbo].[OSUSR_UUK_BAGMSGS""" + year + """] ADD  DEFAULT ('') FOR [JSENTLOC]
ALTER TABLE [dbo].[OSUSR_UUK_BAGMSGS""" + year + """] ADD  DEFAULT ('') FOR [KDMP]
ALTER TABLE [dbo].[OSUSR_UUK_BAGMSGS""" + year + """] ADD  DEFAULT ('') FOR [LPNR]
ALTER TABLE [dbo].[OSUSR_UUK_BAGMSGS""" + year + """] ADD  DEFAULT ('') FOR [NBAGTAG]
ALTER TABLE [dbo].[OSUSR_UUK_BAGMSGS""" + year + """] ADD  DEFAULT ('') FOR [NNRTAGS]
ALTER TABLE [dbo].[OSUSR_UUK_BAGMSGS""" + year + """] ADD  DEFAULT ('') FOR [OFLTNR]
ALTER TABLE [dbo].[OSUSR_UUK_BAGMSGS""" + year + """] ADD  DEFAULT ('1900-01-01 00:00:00') FOR [ODATE]
ALTER TABLE [dbo].[OSUSR_UUK_BAGMSGS""" + year + """] ADD  DEFAULT ('') FOR [ODEST]
ALTER TABLE [dbo].[OSUSR_UUK_BAGMSGS""" + year + """] ADD  DEFAULT ('') FOR [OCLASS]
ALTER TABLE [dbo].[OSUSR_UUK_BAGMSGS""" + year + """] ADD  DEFAULT ('') FOR [PPAXNAME]
ALTER TABLE [dbo].[OSUSR_UUK_BAGMSGS""" + year + """] ADD  DEFAULT ('') FOR [RINTERNAL]
ALTER TABLE [dbo].[OSUSR_UUK_BAGMSGS""" + year + """] ADD  DEFAULT ('') FOR [SAUTL]
ALTER TABLE [dbo].[OSUSR_UUK_BAGMSGS""" + year + """] ADD  DEFAULT ('') FOR [SSEAT]
ALTER TABLE [dbo].[OSUSR_UUK_BAGMSGS""" + year + """] ADD  DEFAULT ('') FOR [SPAXCK]
ALTER TABLE [dbo].[OSUSR_UUK_BAGMSGS""" + year + """] ADD  DEFAULT ('') FOR [SPAXPROF]
ALTER TABLE [dbo].[OSUSR_UUK_BAGMSGS""" + year + """] ADD  DEFAULT ('') FOR [SAUTTRANS]
ALTER TABLE [dbo].[OSUSR_UUK_BAGMSGS""" + year + """] ADD  DEFAULT ('') FOR [SBAGTAGSTATUS]
ALTER TABLE [dbo].[OSUSR_UUK_BAGMSGS""" + year + """] ADD  DEFAULT ('') FOR [TTAGPRINTERID]
ALTER TABLE [dbo].[OSUSR_UUK_BAGMSGS""" + year + """] ADD  DEFAULT ('') FOR [UULD]
ALTER TABLE [dbo].[OSUSR_UUK_BAGMSGS""" + year + """] ADD  DEFAULT ('') FOR [UCOMPT]
ALTER TABLE [dbo].[OSUSR_UUK_BAGMSGS""" + year + """] ADD  DEFAULT ('') FOR [UTYPEOFBAG]
ALTER TABLE [dbo].[OSUSR_UUK_BAGMSGS""" + year + """] ADD  DEFAULT ('') FOR [UDESTCONTAINER]
ALTER TABLE [dbo].[OSUSR_UUK_BAGMSGS""" + year + """] ADD  DEFAULT ('') FOR [UCONTTYPE]
ALTER TABLE [dbo].[OSUSR_UUK_BAGMSGS""" + year + """] ADD  DEFAULT ('') FOR [VBAGSOURCIND]
ALTER TABLE [dbo].[OSUSR_UUK_BAGMSGS""" + year + """] ADD  DEFAULT ('') FOR [VCITY]
ALTER TABLE [dbo].[OSUSR_UUK_BAGMSGS""" + year + """] ADD  DEFAULT ('') FOR [WPWINDICATOR]
ALTER TABLE [dbo].[OSUSR_UUK_BAGMSGS""" + year + """] ADD  DEFAULT ('') FOR [WNRCKBAGS]
ALTER TABLE [dbo].[OSUSR_UUK_BAGMSGS""" + year + """] ADD  DEFAULT ((0)) FOR [WTOTK]
ALTER TABLE [dbo].[OSUSR_UUK_BAGMSGS""" + year + """] ADD  DEFAULT ('') FOR [XSECURITY]
ALTER TABLE [dbo].[OSUSR_UUK_BAGMSGS""" + year + """] ADD  DEFAULT ('') FOR [YFQTV]
ALTER TABLE [dbo].[OSUSR_UUK_BAGMSGS""" + year + """] ADD  DEFAULT ('1900-01-01 00:00:00') FOR [TIMESTAMP]

"""
    return create
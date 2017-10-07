def BAGINTEG(year):
    create = """CREATE TABLE [dbo].[OSUSR_UUK_BAGINTEG""" + year + """](
	[ID] [int] NOT NULL,
	[NUMBER] [nvarchar](13) NULL,
	[ISRUSH] [nvarchar](1) NULL,
	[ISEAT] [nvarchar](3) NULL,
	[IAUT] [nvarchar](1) NULL,
	[IFLTNR] [nvarchar](10) NULL,
	[IDATE] [datetime] NULL,
	[IORIGIN] [nvarchar](3) NULL,
	[BPMIN] [nvarchar](1) NULL,
	[BSMBOARDI] [nvarchar](1) NULL,
	[IATD] [datetime] NULL,
	[IFFP] [nvarchar](1) NULL,
	[FSEAT] [nvarchar](3) NULL,
	[FAUT] [nvarchar](1) NULL,
	[BPMHUB] [nvarchar](1) NULL,
	[BSMBOARD] [nvarchar](1) NULL,
	[FFLTNR] [nvarchar](8) NULL,
	[FDATE] [datetime] NULL,
	[FDEST] [nvarchar](3) NULL,
	[FATD] [datetime] NULL,
	[OFFP] [nvarchar](1) NULL,
	[TIMESTAMP] [datetime] NULL,
	[CLOSE] [nvarchar](1) NULL,
 CONSTRAINT [OSPRK_OSUSR_UUK_BAGINTEG""" + year + """] PRIMARY KEY CLUSTERED 
(
	[ID]
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
ALTER TABLE [dbo].[OSUSR_UUK_BAGINTEG""" + year + """] ADD  DEFAULT ('') FOR [NUMBER]
ALTER TABLE [dbo].[OSUSR_UUK_BAGINTEG""" + year + """] ADD  DEFAULT ('') FOR [ISRUSH]
ALTER TABLE [dbo].[OSUSR_UUK_BAGINTEG""" + year + """] ADD  DEFAULT ('') FOR [ISEAT]
ALTER TABLE [dbo].[OSUSR_UUK_BAGINTEG""" + year + """] ADD  DEFAULT ('') FOR [IAUT]
ALTER TABLE [dbo].[OSUSR_UUK_BAGINTEG""" + year + """] ADD  DEFAULT ('') FOR [IFLTNR]
ALTER TABLE [dbo].[OSUSR_UUK_BAGINTEG""" + year + """] ADD  DEFAULT ('1900-01-01 00:00:00') FOR [IDATE]
ALTER TABLE [dbo].[OSUSR_UUK_BAGINTEG""" + year + """] ADD  DEFAULT ('') FOR [IORIGIN]
ALTER TABLE [dbo].[OSUSR_UUK_BAGINTEG""" + year + """] ADD  DEFAULT ('') FOR [BPMIN]
ALTER TABLE [dbo].[OSUSR_UUK_BAGINTEG""" + year + """] ADD  DEFAULT ('') FOR [BSMBOARDI]
ALTER TABLE [dbo].[OSUSR_UUK_BAGINTEG""" + year + """] ADD  DEFAULT ('1900-01-01 00:00:00') FOR [IATD]
ALTER TABLE [dbo].[OSUSR_UUK_BAGINTEG""" + year + """] ADD  DEFAULT ('') FOR [IFFP]
ALTER TABLE [dbo].[OSUSR_UUK_BAGINTEG""" + year + """] ADD  DEFAULT ('') FOR [FSEAT]
ALTER TABLE [dbo].[OSUSR_UUK_BAGINTEG""" + year + """] ADD  DEFAULT ('') FOR [FAUT]
ALTER TABLE [dbo].[OSUSR_UUK_BAGINTEG""" + year + """] ADD  DEFAULT ('') FOR [BPMHUB]
ALTER TABLE [dbo].[OSUSR_UUK_BAGINTEG""" + year + """] ADD  DEFAULT ('') FOR [BSMBOARD]
ALTER TABLE [dbo].[OSUSR_UUK_BAGINTEG""" + year + """] ADD  DEFAULT ('') FOR [FFLTNR]
ALTER TABLE [dbo].[OSUSR_UUK_BAGINTEG""" + year + """] ADD  DEFAULT ('1900-01-01 00:00:00') FOR [FDATE]
ALTER TABLE [dbo].[OSUSR_UUK_BAGINTEG""" + year + """] ADD  DEFAULT ('') FOR [FDEST]
ALTER TABLE [dbo].[OSUSR_UUK_BAGINTEG""" + year + """] ADD  DEFAULT ('1900-01-01 00:00:00') FOR [FATD]
ALTER TABLE [dbo].[OSUSR_UUK_BAGINTEG""" + year + """] ADD  DEFAULT ('') FOR [OFFP]
ALTER TABLE [dbo].[OSUSR_UUK_BAGINTEG""" + year + """] ADD  DEFAULT ('1900-01-01 00:00:00') FOR [TIMESTAMP]
ALTER TABLE [dbo].[OSUSR_UUK_BAGINTEG""" + year + """] ADD  DEFAULT ('') FOR [CLOSE]

"""
    return create
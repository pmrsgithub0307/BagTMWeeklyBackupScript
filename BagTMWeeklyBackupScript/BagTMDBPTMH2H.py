def PTMH2H(year):
    create = """CREATE TABLE [dbo].[OSUSR_UUK_PTM_H2H""" + year + """](
	[ID] [int] NOT NULL,
	[IFLTNR] [nvarchar](10) NULL,
	[IDATE] [datetime] NULL,
	[IFLTINFOID] [int] NULL,
	[IORIGIN] [nvarchar](3) NULL,
	[STAND] [nvarchar](5) NULL,
	[ETA] [datetime] NULL,
	[SEC] [int] NULL,
	[HUB] [int] NULL,
	[ETCG] [datetime] NULL,
	[ETG] [datetime] NULL,
	[ETGU] [datetime] NULL,
	[OFLTNR] [nvarchar](10) NULL,
	[ODATE] [datetime] NULL,
	[OFLTINFOID] [int] NULL,
	[ODEST] [nvarchar](3) NULL,
	[GATE] [nvarchar](5) NULL,
	[ETD] [datetime] NULL,
	[ECONOMY] [int] NULL,
	[BUSINESS] [int] NULL,
	[FIRST] [int] NULL,
	[STATUS] [nvarchar](3) NULL,
	[DEP] [nvarchar](3) NULL,
 CONSTRAINT [OSPRK_OSUSR_UUK_PTM_H2H""" + year + """] PRIMARY KEY CLUSTERED 
(
	[ID] 
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
ALTER TABLE [dbo].[OSUSR_UUK_PTM_H2H""" + year + """] ADD  DEFAULT ('') FOR [IFLTNR]
ALTER TABLE [dbo].[OSUSR_UUK_PTM_H2H""" + year + """] ADD  DEFAULT ('1900-01-01 00:00:00') FOR [IDATE]
ALTER TABLE [dbo].[OSUSR_UUK_PTM_H2H""" + year + """] ADD  DEFAULT (NULL) FOR [IFLTINFOID]
ALTER TABLE [dbo].[OSUSR_UUK_PTM_H2H""" + year + """] ADD  DEFAULT ('') FOR [IORIGIN]
ALTER TABLE [dbo].[OSUSR_UUK_PTM_H2H""" + year + """] ADD  DEFAULT ('') FOR [STAND]
ALTER TABLE [dbo].[OSUSR_UUK_PTM_H2H""" + year + """] ADD  DEFAULT ('1900-01-01 00:00:00') FOR [ETA]
ALTER TABLE [dbo].[OSUSR_UUK_PTM_H2H""" + year + """] ADD  DEFAULT ((0)) FOR [SEC]
ALTER TABLE [dbo].[OSUSR_UUK_PTM_H2H""" + year + """] ADD  DEFAULT ((0)) FOR [HUB]
ALTER TABLE [dbo].[OSUSR_UUK_PTM_H2H""" + year + """] ADD  DEFAULT ('1900-01-01 00:00:00') FOR [ETCG]
ALTER TABLE [dbo].[OSUSR_UUK_PTM_H2H""" + year + """] ADD  DEFAULT ('1900-01-01 00:00:00') FOR [ETG]
ALTER TABLE [dbo].[OSUSR_UUK_PTM_H2H""" + year + """] ADD  DEFAULT ('1900-01-01 00:00:00') FOR [ETGU]
ALTER TABLE [dbo].[OSUSR_UUK_PTM_H2H""" + year + """] ADD  DEFAULT ('') FOR [OFLTNR]
ALTER TABLE [dbo].[OSUSR_UUK_PTM_H2H""" + year + """] ADD  DEFAULT ('1900-01-01 00:00:00') FOR [ODATE]
ALTER TABLE [dbo].[OSUSR_UUK_PTM_H2H""" + year + """] ADD  DEFAULT (NULL) FOR [OFLTINFOID]
ALTER TABLE [dbo].[OSUSR_UUK_PTM_H2H""" + year + """] ADD  DEFAULT ('') FOR [ODEST]
ALTER TABLE [dbo].[OSUSR_UUK_PTM_H2H""" + year + """] ADD  DEFAULT ('') FOR [GATE]
ALTER TABLE [dbo].[OSUSR_UUK_PTM_H2H""" + year + """] ADD  DEFAULT ('1900-01-01 00:00:00') FOR [ETD]
ALTER TABLE [dbo].[OSUSR_UUK_PTM_H2H""" + year + """] ADD  DEFAULT ((0)) FOR [ECONOMY]
ALTER TABLE [dbo].[OSUSR_UUK_PTM_H2H""" + year + """] ADD  DEFAULT ((0)) FOR [BUSINESS]
ALTER TABLE [dbo].[OSUSR_UUK_PTM_H2H""" + year + """] ADD  DEFAULT ((0)) FOR [FIRST]
ALTER TABLE [dbo].[OSUSR_UUK_PTM_H2H""" + year + """] ADD  DEFAULT ('') FOR [STATUS]
ALTER TABLE [dbo].[OSUSR_UUK_PTM_H2H""" + year + """] ADD  DEFAULT ('') FOR [DEP]

"""
    return create
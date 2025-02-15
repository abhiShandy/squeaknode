import { makeStyles } from '@material-ui/styles';

export default makeStyles((theme) => ({
  widgetWrapper: {
    display: 'flex',
    minHeight: '100%',
  },
  widgetHeader: {
    padding: theme.spacing(3),
    paddingBottom: theme.spacing(1),
    display: 'flex',
    justifyContent: 'space-between',
    alignItems: 'center',
  },
  widgetRoot: {
    boxShadow: theme.customShadows.widget,
  },
  widgetBody: {
    paddingBottom: theme.spacing(3),
    paddingRight: theme.spacing(3),
    paddingLeft: theme.spacing(3),
  },
  noPadding: {
    padding: 0,
  },
  paper: {
    padding: '6px 12px',
  },
  secondaryTail: {
    backgroundColor: theme.palette.secondary.main,
  },
  moreButton: {
    margin: -theme.spacing(1),
    padding: 0,
    width: 40,
    height: 40,
    color: theme.palette.text.hint,
    '&:hover': {
      backgroundColor: theme.palette.primary.main,
      color: 'rgba(255, 255, 255, 0.35)',
    },
  },
  root: {
    maxWidth: 345,
  },
  media: {
    height: 180,
  },
}));

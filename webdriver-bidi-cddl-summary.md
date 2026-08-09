# WebDriver BiDi - API & Schema Summary

> Sintesi gerarchica del protocollo W3C per contesto LLM.



# 1. # Protocol #

This section defines the basic concepts of the WebDriver BiDi
protocol. These terms are distinct from their representation at the
transport layer.


## 1.1. ## Definition ##

This section gives the initial contents of the {^remote end definition^} and
{^local end definition^}. These are augmented by the definition fragments defined in
the remainder of the specification.

> [!IMPORTANT]
> Should this be an appendix?

```cddl
Command = {
  id: js-uint,
  CommandData,
  Extensible,
}

CommandData = (
  BrowserCommand //
  BrowsingContextCommand //
  EmulationCommand //
  InputCommand //
  NetworkCommand //
  ScriptCommand //
  SessionCommand //
  StorageCommand //
  WebExtensionCommand
)

EmptyParams = {
   Extensible
}
```

```cddl
Message = (
  CommandResponse /
  ErrorResponse /
  Event
)

CommandResponse = {
  type: "success",
  id: js-uint,
  result: ResultData,
  Extensible
}

ErrorResponse = {
  type: "error",
  id: js-uint / null,
  error: ErrorCode,
  message: text,
  ? stacktrace: text,
  Extensible
}

ResultData = (
  BrowserResult /
  BrowsingContextResult /
  EmulationResult /
  InputResult /
  NetworkResult /
  ScriptResult /
  SessionResult /
  StorageResult /
  WebExtensionResult
)

EmptyResult = {
  Extensible
}

Event = {
  type: "event",
  EventData,
  Extensible
}

EventData = (
  BrowsingContextEvent //
  InputEvent //
  LogEvent //
  NetworkEvent //
  ScriptEvent
)
```

```cddl
Extensible = (*text => any)

js-int = -9007199254740991..9007199254740991
js-uint = 0..9007199254740991
```


## 1.2. ## Modules ##

The WebDriver BiDi protocol is organized into modules.


## 1.3. ## Commands ##

A command is an asynchronous operation, requested by
the local end and run on the remote end, resulting in either a
result or an error being returned to the local end. Multiple
commands can run at the same time, and commands can potentially be
long-running. As a consequence, commands can finish out-of-order.

> [!NOTE]
> This is because the command id is entirely controlled by the local end
and isn't necessarily unique over the course of a session. For example a local
end which ignores all responses could use the same command id for each command.


## 1.4. ## Errors ##

WebDriver BiDi extends the set of error codes from [[WEBDRIVER|WebDriver]]
with the following additional codes:

```cddl
ErrorCode = "invalid argument" /
            "invalid selector" /
            "invalid session id" /
            "invalid web extension" /
            "move target out of bounds" /
            "no such alert" /
            "no such network collector" /
            "no such element" /
            "no such frame" /
            "no such handle" /
            "no such history entry" /
            "no such intercept" /
            "no such network data" /
            "no such node" /
            "no such request" /
            "no such screencast" /
            "no such script" /
            "no such storage partition" /
            "no such user context" /
            "no such web extension" /
            "session not created" /
            "unable to capture screen" /
            "unable to close browser" /
            "unable to set cookie" /
            "unable to set file input" /
            "unavailable network data" /
            "underspecified storage partition" /
            "unknown command" /
            "unknown error" /
            "unsupported operation"
```


## 1.5. ## Events ##

An event is a notification, sent by the remote end
to the local end, signaling that something of interest has
occurred on the remote end.


## 2.1. ## The session Module ##

The session module contains commands and
events for monitoring the status of the remote end.


### 2.1.1. ### Definition ###

**Algorithm: To end the sessiongiven |session|**
To end the session given |session|:
1. Remove |session| from active sessions.
1. If active sessions is list/empty, set the webdriver-active flag
to false.

```cddl
SessionCommand = (
  session.End //
  session.New //
  session.Status //
  session.Subscribe //
  session.Unsubscribe
)
```

```cddl
SessionResult = (
  session.EndResult /
  session.NewResult /
  session.StatusResult /
  session.SubscribeResult /
  session.UnsubscribeResult
)
```


#### 2.1.2.1. #### The session.CapabilitiesRequest Type ####

The session.CapabilitiesRequest type represents the capabilities requested
for a session.

```cddl
session.CapabilitiesRequest = {
  ? alwaysMatch: session.CapabilityRequest,
  ? firstMatch: [*session.CapabilityRequest]
}
```


#### 2.1.2.2. #### The session.CapabilityRequest Type ####

The session.CapabilityRequest type represents a specific set of
requested capabilities.

```cddl
session.CapabilityRequest = {
  ? acceptInsecureCerts: bool,
  ? browserName: text,
  ? browserVersion: text,
  ? platformName: text,
  ? proxy: session.ProxyConfiguration,
  ? unhandledPromptBehavior: session.UserPromptHandler,
  Extensible
}
```


#### 2.1.2.3. #### The session.ProxyConfiguration Type ####

session.AutodetectProxyConfiguration = (
 proxyType: "autodetect",
 Extensible
)

```cddl
session.ProxyConfiguration = {
   session.AutodetectProxyConfiguration //
   session.DirectProxyConfiguration //
   session.ManualProxyConfiguration //
   session.PacProxyConfiguration //
   session.SystemProxyConfiguration
}

session.AutodetectProxyConfiguration = (
   proxyType: "autodetect",
   Extensible
)

session.DirectProxyConfiguration = (
   proxyType: "direct",
   Extensible
)

session.ManualProxyConfiguration = (
   proxyType: "manual",
   ? httpProxy: text,
   ? sslProxy: text,
   ? session.SocksProxyConfiguration,
   ? noProxy: [*text],
   Extensible
)

session.SocksProxyConfiguration = (
   socksProxy: text,
   socksVersion: 0..255,
)

session.PacProxyConfiguration = (
   proxyType: "pac",
   proxyAutoconfigUrl: text,
   Extensible
)

session.SystemProxyConfiguration = (
   proxyType: "system",
   Extensible
)
```


#### 2.1.2.4. #### The session.UserPromptHandler Type ####

The session.UserPromptHandler type represents the configuration of
the user prompt handler.

> [!NOTE]
> file handles file picker. "accept" and "dismiss" dismisses
the picker. "ignore" keeps the picker open.

```cddl
session.UserPromptHandler = {
  ? alert: session.UserPromptHandlerType,
  ? beforeUnload: session.UserPromptHandlerType,
  ? confirm: session.UserPromptHandlerType,
  ? default: session.UserPromptHandlerType,
  ? file: session.UserPromptHandlerType,
  ? prompt: session.UserPromptHandlerType,
}
```


#### 2.1.2.5. #### The session.UserPromptHandlerType Type ####

The session.UserPromptHandlerType type represents the behavior
of the user prompt handler.

```cddl
session.UserPromptHandlerType = "accept" / "dismiss" / "ignore";
```


#### 2.1.2.6. #### The session.Subscription Type ####

The session.Subscription type represents a unique subscription identifier.

```cddl
session.Subscription = text
```


#### 2.1.2.7. #### The session.SubscribeParameters Type ####

The session.SubscribeParameters type represents a request to
subscribe to a specific set of events.

```cddl
session.SubscribeParameters = {
  events: [+text],
  ? contexts: [+browsingContext.BrowsingContext],
  ? userContexts: [+browser.UserContext],
}
```


#### 2.1.2.8. #### The session.UnsubscribeByIDRequest Type ####

The session.UnsubscribeByIDRequest type represents a request to
remove event subscriptions identified by subscription IDs.

```cddl
session.UnsubscribeByIDRequest = {
  subscriptions: [+session.Subscription],
}
```


#### 2.1.2.9. #### The session.UnsubscribeByAttributesRequest Type ####

The session.UnsubscribeByAttributesRequest type represents a request to
unsubscribe using subscription attributes.

```cddl
session.UnsubscribeByAttributesRequest = {
  events: [+text],
}
```


#### 2.1.3.1. #### The session.status Command ####

The session.status command returns information about
whether a remote end is in a state in which it can create new sessions,
but may additionally include arbitrary meta information that is specific
to the implementation.

```cddl
session.Status = (
        method: "session.status",
        params: EmptyParams,
      )
```

```cddl
session.StatusResult = {
        ready: bool,
        message: text,
      }
```


#### 2.1.3.2. #### The session.new Command ####

The session.new command allows creating a new
BiDi session.

> [!NOTE]
> A session created this way will not be accessible via HTTP.

```cddl
session.New = (
        method: "session.new",
        params: session.NewParameters
      )

      session.NewParameters = {
        capabilities: session.CapabilitiesRequest
      }
```

```cddl
session.NewResult = {
        sessionId: text,
        capabilities: {
          acceptInsecureCerts: bool,
          browserName: text,
          browserVersion: text,
          platformName: text,
          setWindowRect: bool,
          userAgent: text,
          ? proxy: session.ProxyConfiguration,
          ? unhandledPromptBehavior: session.UserPromptHandler,
          ? webSocketUrl: text,
          Extensible
        }
      }
```


#### 2.1.3.3. #### The session.end Command ####

The session.end command ends the current
/session.

```cddl
session.End = (
        method: "session.end",
        params: EmptyParams
      )
```

```cddl
session.EndResult = EmptyResult
```


#### 2.1.3.4. #### The session.subscribe Command ####

The session.subscribe command enables certain events
either globally or for a set of navigables.

> [!IMPORTANT]
> This needs to be generalized to work with realms too.

```cddl
session.Subscribe = (
        method: "session.subscribe",
        params: session.SubscribeParameters
      )
```

```cddl
session.SubscribeResult = {
          subscription: session.Subscription,
        }
```


#### 2.1.3.5. #### The session.unsubscribe Command ####

The session.unsubscribe command disables events
either globally or for a set of navigables.

> [!IMPORTANT]
> This needs to be generalised to work with realms too.

```cddl
session.Unsubscribe = (
       method: "session.unsubscribe",
       params: session.UnsubscribeParameters,
     )

     session.UnsubscribeParameters = session.UnsubscribeByAttributesRequest / session.UnsubscribeByIDRequest
```

```cddl
session.UnsubscribeResult = EmptyResult
```


## 2.2. ## The browser Module ##

The browser module contains commands for
managing the remote end browser process.


### 2.2.1. ### Definition ###

BrowserResult = (
 browser.CloseResult /
 browser.CreateUserContextResult /
 browser.GetClientWindowsResult /
 browser.GetUserContextsResult /
 browser.RemoveUserContextResult /
 browser.SetClientWindowStateResult /
 browser.SetDownloadBehaviorResult
)

```cddl
BrowserCommand = (
  browser.Close //
  browser.CreateUserContext //
  browser.GetClientWindows //
  browser.GetUserContexts //
  browser.RemoveUserContext //
  browser.SetClientWindowState //
  browser.SetDownloadBehavior
)
```

```cddl
BrowserResult = (
  browser.CloseResult /
  browser.CreateUserContextResult /
  browser.GetClientWindowsResult /
  browser.GetUserContextsResult /
  browser.RemoveUserContextResult /
  browser.SetClientWindowStateResult /
  browser.SetDownloadBehaviorResult
)
```


#### 2.2.2.1. #### The browser.ClientWindow Type ####

The browser.ClientWindow uniquely identifies a client window.

```cddl
browser.ClientWindow = text;
```


#### 2.2.2.2. #### The browser.ClientWindowInfo Type ####

The browser.ClientWindowInfo type represents properties of a
client window.

```cddl
browser.ClientWindowInfo = {
  active: bool,
  clientWindow: browser.ClientWindow,
  height: js-uint,
  state: "fullscreen" / "maximized" / "minimized" / "normal",
  width: js-uint,
  x: js-int,
  y: js-int,
}
```


#### 2.2.2.3. #### The browser.UserContext Type ####

The browser.UserContext unique identifies a user context.

```cddl
browser.UserContext = text;
```


#### 2.2.2.4. #### The browser.UserContextInfo Type ####

The browser.UserContextInfo type represents properties of a user
context.

```cddl
browser.UserContextInfo = {
  userContext: browser.UserContext
}
```


#### 2.2.3.1. #### The browser.close Command ####

The browser.close command terminates all
WebDriver sessions and cleans up automation state in the remote browser instance.

```cddl
browser.Close = (
        method: "browser.close",
        params: EmptyParams,
      )
```

```cddl
browser.CloseResult = EmptyResult
```


#### 2.2.3.2. #### The browser.createUserContext Command ####

The browser.createUserContext command creates a
user context.

```cddl
browser.CreateUserContext = (
        method: "browser.createUserContext",
        params: browser.CreateUserContextParameters,
      )

      browser.CreateUserContextParameters = {
        ? acceptInsecureCerts: bool,
        ? proxy: session.ProxyConfiguration,
        ? unhandledPromptBehavior: session.UserPromptHandler
      }
```

```cddl
browser.CreateUserContextResult = browser.UserContextInfo
```


#### 2.2.3.3. #### The browser.getClientWindows Command ####

The browser.getClientWindows command returns a
list of client windows.

```cddl
browser.GetClientWindows = (
        method: "browser.getClientWindows",
        params: EmptyParams,
      )
```

```cddl
browser.GetClientWindowsResult = {
        clientWindows: [ * browser.ClientWindowInfo]
      }
```


#### 2.2.3.4. #### The browser.getUserContexts Command ####

The browser.getUserContexts command returns a
list of user contexts.

```cddl
browser.GetUserContexts = (
        method: "browser.getUserContexts",
        params: EmptyParams,
      )
```

```cddl
browser.GetUserContextsResult = {
        userContexts: [ + browser.UserContextInfo]
      }
```


#### 2.2.3.5. #### The browser.removeUserContext Command ####

The browser.removeUserContext command closes a
user context and all navigables in it without running
beforeunload handlers.

```cddl
browser.RemoveUserContext = (
        method: "browser.removeUserContext",
        params: browser.RemoveUserContextParameters
      )

      browser.RemoveUserContextParameters = {
        userContext: browser.UserContext
      }
```

```cddl
browser.RemoveUserContextResult = EmptyResult
```


#### 2.2.3.6. #### The browser.setClientWindowState Command ####

The browser.setClientWindowState command sets the
dimensions of a client window.

```cddl
browser.SetClientWindowState = (
        method: "browser.setClientWindowState",
        params: browser.SetClientWindowStateParameters
      )

      browser.SetClientWindowStateParameters = {
        clientWindow: browser.ClientWindow,
        (browser.ClientWindowNamedState // browser.ClientWindowRectState)
      }

      browser.ClientWindowNamedState = (
        state: "fullscreen" / "maximized" / "minimized"
      )

      browser.ClientWindowRectState = (
        state: "normal",
        ? width: js-uint,
        ? height: js-uint,
        ? x: js-int,
        ? y: js-int,
      )
```

```cddl
browser.SetClientWindowStateResult = browser.ClientWindowInfo
```


#### 2.2.3.7. #### The browser.setDownloadBehavior Command ####

A download behavior struct is a struct with:
* struct/item named allowed which is a boolean;
* struct/item named destinationFolder which is a string or null.

```cddl
browser.SetDownloadBehavior = (
        method: "browser.setDownloadBehavior",
        params: browser.SetDownloadBehaviorParameters
      )

      browser.SetDownloadBehaviorParameters = {
        downloadBehavior: browser.DownloadBehavior / null,
        ? userContexts: [+browser.UserContext]
      }

      browser.DownloadBehavior = {
        (
          browser.DownloadBehaviorAllowed //
          browser.DownloadBehaviorDenied
        )
      }

      browser.DownloadBehaviorAllowed = (
        type: "allowed",
        destinationFolder: text
      )

      browser.DownloadBehaviorDenied = (
        type: "denied"
      )
```

```cddl
browser.SetDownloadBehaviorResult = EmptyResult
```


## 2.3. ## The browsingContext Module ##

The browsingContext module contains commands and
events relating to /navigables.

> [!NOTE]
> For historic reasons this module is called browsingContext
rather than navigable, and the protocol uses the term
context to refer to navigables, particularly as a field in command
and response parameters.


### 2.3.1. ### Definition ###

BrowsingContextEvent = (
 browsingContext.ContextCreated //
 browsingContext.ContextDestroyed //
 browsingContext.DomContentLoaded //
 browsingContext.DownloadEnd //
 browsingContext.DownloadWillBegin //
 browsingContext.FragmentNavigated //
 browsingContext.HistoryUpdated //
 browsingContext.Load //
 browsingContext.NavigationAborted //
 browsingContext.NavigationCommitted //
 browsingContext.NavigationFailed //
 browsingContext.NavigationStarted //
 browsingContext.UserPromptClosed //
 browsingContext.UserPromptOpened
)

> [!NOTE]
> this map is not cleared when the final session ends i.e. device pixel
ratio overrides outlive any WebDriver session.

```cddl
BrowsingContextCommand = (
  browsingContext.Activate //
  browsingContext.CaptureScreenshot //
  browsingContext.Close //
  browsingContext.Create //
  browsingContext.GetTree //
  browsingContext.HandleUserPrompt //
  browsingContext.LocateNodes //
  browsingContext.Navigate //
  browsingContext.Print //
  browsingContext.Reload //
  browsingContext.SetBypassCSP //
  browsingContext.SetViewport //
  browsingContext.StartScreencast //
  browsingContext.StopScreencast //
  browsingContext.TraverseHistory
)
```

```cddl
BrowsingContextResult = (
  browsingContext.ActivateResult /
  browsingContext.CaptureScreenshotResult /
  browsingContext.CloseResult /
  browsingContext.CreateResult /
  browsingContext.GetTreeResult /
  browsingContext.HandleUserPromptResult /
  browsingContext.LocateNodesResult /
  browsingContext.NavigateResult /
  browsingContext.PrintResult /
  browsingContext.ReloadResult /
  browsingContext.SetBypassCSPResult /
  browsingContext.SetViewportResult /
  browsingContext.StartScreencastResult /
  browsingContext.StopScreencastResult /
  browsingContext.TraverseHistoryResult
)

BrowsingContextEvent = (
  browsingContext.ContextCreated //
  browsingContext.ContextDestroyed //
  browsingContext.DomContentLoaded //
  browsingContext.DownloadEnd //
  browsingContext.DownloadWillBegin //
  browsingContext.FragmentNavigated //
  browsingContext.HistoryUpdated //
  browsingContext.Load //
  browsingContext.NavigationAborted //
  browsingContext.NavigationCommitted //
  browsingContext.NavigationFailed //
  browsingContext.NavigationStarted //
  browsingContext.UserPromptClosed //
  browsingContext.UserPromptOpened
)
```


#### 2.3.2.1. #### The browsingContext.BrowsingContext Type ####

Each /navigable has an associated navigable id,
which is a string uniquely identifying that navigable. This is
implicitly set when the navigable is created. For navigables with an
associated WebDriver window handle the /navigable id must be the
same as the window handle.

```cddl
browsingContext.BrowsingContext = text;
```


#### 2.3.2.2. #### The browsingContext.Info Type ####

browsingContext.Info = {
 children: browsingContext.InfoList / null,
 clientWindow: browser.ClientWindow,
 context: browsingContext.BrowsingContext,
 originalOpener: browsingContext.BrowsingContext / null,
 url: text,
 userContext: browser.UserContext,
 ? parent: browsingContext.BrowsingContext / null,
}

```cddl
browsingContext.InfoList = [*browsingContext.Info]

browsingContext.Info = {
  children: browsingContext.InfoList / null,
  clientWindow: browser.ClientWindow,
  context: browsingContext.BrowsingContext,
  originalOpener: browsingContext.BrowsingContext / null,
  url: text,
  userContext: browser.UserContext,
  ? parent: browsingContext.BrowsingContext / null,
}
```


#### 2.3.2.3. #### The browsingContext.Locator Type ####

browsingContext.AccessibilityLocator = {
 type: "accessibility",
 value: {
 ? name: text,
 ? role: text,
 }
}

```cddl
browsingContext.Locator = (
   browsingContext.AccessibilityLocator /
   browsingContext.CssLocator /
   browsingContext.ContextLocator /
   browsingContext.InnerTextLocator /
   browsingContext.XPathLocator
)

browsingContext.AccessibilityLocator = {
   type: "accessibility",
   value: {
    ? name: text,
    ? role: text,
   }
}

browsingContext.CssLocator = {
   type: "css",
   value: text
}

browsingContext.ContextLocator = {
  type: "context",
  value: {
    context: browsingContext.BrowsingContext,
  }
}

browsingContext.InnerTextLocator = {
   type: "innerText",
   value: text,
   ? ignoreCase: bool
   ? matchType: "full" / "partial",
   ? maxDepth: js-uint,
}

browsingContext.XPathLocator = {
   type: "xpath",
   value: text
}
```


#### 2.3.2.4. #### The browsingContext.Navigation Type ####

The browsingContext.Navigation type is a unique string identifying an ongoing
navigation.

```cddl
browsingContext.Navigation = text;
```


#### 2.3.2.5. #### The browsingContext.Download Type ####

The browsingContext.Download type is a unique string identifying a download.

```cddl
browsingContext.Download = text;
```


#### 2.3.2.6. #### The browsingContext.NavigationInfo Type ####

browsingContext.NavigationInfo = {
 browsingContext.BaseNavigationInfo
}

```cddl
browsingContext.BaseNavigationInfo = (
  context: browsingContext.BrowsingContext,
  navigation: browsingContext.Navigation / null,
  timestamp: js-uint,
  url: text,
  ? userContext: browser.UserContext,
)

browsingContext.NavigationInfo = {
  browsingContext.BaseNavigationInfo
}
```


#### 2.3.2.7. #### The browsingContext.ReadinessState Type ####

The browsingContext.ReadinessState type represents the stage of
document loading at which a navigation command will return.

```cddl
browsingContext.ReadinessState = "none" / "interactive" / "complete"
```


#### 2.3.2.8. #### The browsingContext.UserPromptType Type ####

The browsingContext.UserPromptType type represents the possible user
prompt types.

```cddl
browsingContext.UserPromptType = "alert" / "beforeunload" / "confirm" / "prompt";
```


#### 2.3.3.1. #### The browsingContext.activate Command ####

The browsingContext.activate command activates and focuses the given /top-level traversable.

```cddl
browsingContext.Activate = (
        method: "browsingContext.activate",
        params: browsingContext.ActivateParameters
      )

      browsingContext.ActivateParameters = {
        context: browsingContext.BrowsingContext
      }
```

```cddl
browsingContext.ActivateResult = EmptyResult
```


#### 2.3.3.2. #### The browsingContext.captureScreenshot Command ####

The browsingContext.captureScreenshot command
captures an image of the given navigable, and returns it as a
Base64-encoded string.

> [!IMPORTANT]
> This ought to be integrated into the update
 rendering algorithm in some more explicit way.

```cddl
browsingContext.CaptureScreenshot = (
        method: "browsingContext.captureScreenshot",
        params: browsingContext.CaptureScreenshotParameters
      )

      browsingContext.CaptureScreenshotParameters = {
        context: browsingContext.BrowsingContext,
        ? origin: ("viewport" / "document") .default "viewport",
        ? format: browsingContext.ImageFormat,
        ? clip: browsingContext.ClipRectangle,
      }

      browsingContext.ImageFormat = {
         type: text,
         ? quality: 0.0..1.0,
      }

      browsingContext.ClipRectangle = (
        browsingContext.BoxClipRectangle /
        browsingContext.ElementClipRectangle
      )

      browsingContext.ElementClipRectangle = {
        type: "element",
        element: script.SharedReference
      }

      browsingContext.BoxClipRectangle = {
         type: "box",
         x: float,
         y: float,
         width: float,
         height: float
      }
```

```cddl
browsingContext.CaptureScreenshotResult = {
          data: text
        }
```


#### 2.3.3.3. #### The browsingContext.close Command ####

The browsingContext.close command closes a
/top-level traversable.

```cddl
browsingContext.Close = (
        method: "browsingContext.close",
        params: browsingContext.CloseParameters
      )

      browsingContext.CloseParameters = {
        context: browsingContext.BrowsingContext,
        ? promptUnload: bool .default false
      }
```

```cddl
browsingContext.CloseResult = EmptyResult
```


#### 2.3.3.4. #### The browsingContext.create Command ####

The browsingContext.create command creates a new
/navigable, either in a new tab or in a new window, and returns its
navigable id.

```cddl
browsingContext.Create = (
        method: "browsingContext.create",
        params: browsingContext.CreateParameters
      )

      browsingContext.CreateType = "tab" / "window"

      browsingContext.CreateParameters = {
        type: browsingContext.CreateType,
        ? referenceContext: browsingContext.BrowsingContext,
        ? background: bool .default false,
        ? userContext: browser.UserContext
      }
```

```cddl
browsingContext.CreateResult = {
          context: browsingContext.BrowsingContext,
          ? userContext: browser.UserContext
        }
```


#### 2.3.3.5. #### The browsingContext.getTree Command ####

The browsingContext.getTree command returns a
tree of all descendent navigables including the given parent itself,
or all top-level contexts when no parent is provided.

```cddl
browsingContext.GetTree = (
        method: "browsingContext.getTree",
        params: browsingContext.GetTreeParameters
      )

      browsingContext.GetTreeParameters = {
        ? maxDepth: js-uint,
        ? root: browsingContext.BrowsingContext,
      }
```

```cddl
browsingContext.GetTreeResult = {
          contexts: browsingContext.InfoList
        }
```


#### 2.3.3.6. #### The browsingContext.handleUserPrompt Command ####

The browsingContext.handleUserPrompt
command allows closing an open prompt

```cddl
browsingContext.HandleUserPrompt = (
        method: "browsingContext.handleUserPrompt",
        params: browsingContext.HandleUserPromptParameters
      )

      browsingContext.HandleUserPromptParameters = {
        context: browsingContext.BrowsingContext,
        ? accept: bool,
        ? userText: text,
      }
```

```cddl
browsingContext.HandleUserPromptResult = EmptyResult
```


#### 2.3.3.7. #### The browsingContext.locateNodes Command ####

The browsingContext.locateNodes command returns a
list of all nodes matching the specified locator.

```cddl
browsingContext.LocateNodes = (
        method: "browsingContext.locateNodes",
        params: browsingContext.LocateNodesParameters
      )

      browsingContext.LocateNodesParameters = {
         context: browsingContext.BrowsingContext,
         locator: browsingContext.Locator,
         ? maxNodeCount: (js-uint .ge 1),
         ? serializationOptions: script.SerializationOptions,
         ? startNodes: [ + script.SharedReference ]
      }
```

```cddl
browsingContext.LocateNodesResult = {
            nodes: [ * script.NodeRemoteValue ]
        }
```


#### 2.3.3.8. #### The browsingContext.navigate Command ####

The browsingContext.navigate command navigates a
navigable to the given URL.

```cddl
browsingContext.Navigate = (
        method: "browsingContext.navigate",
        params: browsingContext.NavigateParameters
      )

      browsingContext.NavigateParameters = {
        context: browsingContext.BrowsingContext,
        url: text,
        ? wait: browsingContext.ReadinessState,
      }
```

```cddl
browsingContext.NavigateResult = {
          navigation: browsingContext.Navigation / null,
          url: text,
        }
```


#### 2.3.3.9. #### The browsingContext.print Command ####

The browsingContext.print command
creates a paginated representation of a document, and returns it as a
PDF document represented as a Base64-encoded string.

```cddl
browsingContext.Print = (
        method: "browsingContext.print",
        params: browsingContext.PrintParameters
      )

      browsingContext.PrintParameters = {
        context: browsingContext.BrowsingContext,
        ? background: bool .default false,
        ? margin: browsingContext.PrintMarginParameters,
        ? orientation: ("portrait" / "landscape") .default "portrait",
        ? page: browsingContext.PrintPageParameters,
        ? pageRanges: [*(js-uint / text)],
        ? scale: (0.1..2.0) .default 1.0,
        ? shrinkToFit: bool .default true,
      }

      browsingContext.PrintMarginParameters = {
        ? bottom: (float .ge 0.0) .default 1.0,
        ? left: (float .ge 0.0) .default 1.0,
        ? right: (float .ge 0.0) .default 1.0,
        ? top: (float .ge 0.0) .default 1.0,
      }

      ; Minimum size is 1pt x 1pt. Conversion follows from
      ; https://www.w3.org/TR/css3-values/#absolute-lengths
      browsingContext.PrintPageParameters = {
        ? height: (float .ge 0.0352) .default 27.94,
        ? width: (float .ge 0.0352) .default 21.59,
      }
```

```cddl
browsingContext.PrintResult = {
          data: text
        }
```


#### 2.3.3.10. #### The browsingContext.reload Command ####

The browsingContext.reload command reloads a
navigable.

```cddl
browsingContext.Reload = (
        method: "browsingContext.reload",
        params: browsingContext.ReloadParameters
      )

      browsingContext.ReloadParameters = {
        context: browsingContext.BrowsingContext,
        ? ignoreCache: bool,
        ? wait: browsingContext.ReadinessState,
      }
```

```cddl
browsingContext.ReloadResult = browsingContext.NavigateResult
```


#### 2.3.3.11. #### The browsingContext.setBypassCSP Command ####

The browsingContext.setBypassCSP command allows bypassing Content Security Policy enforcement.

> [!NOTE]
> When CSP bypass is enabled, all CSP directives are bypassed, including those that would normally block eval(), new Function(), inline scripts, and resource loading.

```cddl
browsingContext.SetBypassCSP = (
        method: "browsingContext.setBypassCSP",
        params: browsingContext.SetBypassCSPParameters
      )

      browsingContext.SetBypassCSPParameters = {
        bypass: true / null,
        ? contexts: [+browsingContext.BrowsingContext],
        ? userContexts: [+browser.UserContext],
      }
```

```cddl
browsingContext.SetBypassCSPResult = EmptyResult
```


#### 2.3.3.12. #### The browsingContext.setViewport Command ####

The browsingContext.setViewport command modifies specific viewport characteristics (e.g. viewport width and viewport height) on the given top-level traversable.

```cddl
browsingContext.SetViewport = (
        method: "browsingContext.setViewport",
        params: browsingContext.SetViewportParameters
      )

      browsingContext.SetViewportParameters = {
        ? context: browsingContext.BrowsingContext,
        ? viewport: browsingContext.Viewport / null,
        ? devicePixelRatio: (float .gt 0.0) / null,
        ? userContexts: [+browser.UserContext],
      }

      browsingContext.Viewport = {
        width: js-uint,
        height: js-uint,
      }
```

```cddl
browsingContext.SetViewportResult = EmptyResult
```


#### 2.3.3.13. #### The browsingContext.startScreencast Command ####

The browsingContext.startScreencast command
starts the screencast of a given navigable and writes it to a file.

> [!NOTE]
> The remote end creates and writes the screencast file, but does not delete it.
Cleaning up the file is left to the local end. In some configurations this might not be
possible — for example, if the remote end has read/write access to the filesystem but
the local end has only read-only access.

```cddl
browsingContext.StartScreencast = (
        method: "browsingContext.startScreencast",
        params: browsingContext.StartScreencastParameters
      )

      browsingContext.StartScreencastParameters = {
        context: browsingContext.BrowsingContext,
        ? mimeType: text,
        ? video: browsingContext.MediaTrackConstraints,
        ? audio: bool .default false,
      }

      browsingContext.MediaTrackConstraints = {
         ? width: js-uint,
         ? height: js-uint,
         ? frameRate: js-uint,
      }
```

```cddl
browsingContext.StartScreencastResult = {
         screencast: browsingContext.Screencast,
         path: text
      }
```

```cddl
browsingContext.Screencast = text
```


#### 2.3.3.14. #### The browsingContext.stopScreencast Command ####

The browsingContext.stopScreencast command
stops the screencast.

```cddl
browsingContext.StopScreencast = (
        method: "browsingContext.stopScreencast",
        params: browsingContext.StopScreencastParameters
      )

      browsingContext.StopScreencastParameters = {
        screencast: browsingContext.Screencast
      }
```

```cddl
browsingContext.StopScreencastResult = {
         path: text,
         ? error: text
      }
```


#### 2.3.3.15. #### The browsingContext.traverseHistory Command ####

The browsingContext.traverseHistory command
traverses the history of a given navigable by a delta.

```cddl
browsingContext.TraverseHistory = (
        method: "browsingContext.traverseHistory",
        params: browsingContext.TraverseHistoryParameters
      )

      browsingContext.TraverseHistoryParameters = {
        context: browsingContext.BrowsingContext,
        delta: js-int,
      }
```

```cddl
browsingContext.TraverseHistoryResult = EmptyResult
```


#### 2.3.4.1. #### The browsingContext.contextCreated Event ####

**Algorithm: To Recursively emit context created eventsgiven |session| and |navigable|**
To Recursively emit context created events given |session| and |navigable|:
1. Emit a context created event with |session| and |navigable|.
1. For each child navigable, |child|, of |navigable|:
 1. Recursively emit context created events given |session| and |child|.

```cddl
browsingContext.ContextCreated = (
         method: "browsingContext.contextCreated",
         params: browsingContext.Info
        )
```


#### 2.3.4.2. #### The browsingContext.contextDestroyed Event ####

The remote end event trigger is
the WebDriver BiDi navigable destroyed steps given /navigable |navigable|:
1. Let |params| be the result of get the navigable info, given
|navigable|, null, and true.
1. Let |body| be a /map matching the
browsingContext.ContextDestroyed production, with the
params field set to |params|.
1. Let |related navigables| be a /set containing |navigable|'s navigable/parent,
if that is not null, or an empty /set otherwise.
1. For each |session| in the set of sessions for which an event is enabled
given "browsingContext.contextDestroyed" and |related navigables|:
 1. Emit an event with |session| and |body|.
 1. Let |subscriptions to remove| be a /set.
 1. For each |subscription| in |session|'s subscriptions:
 1. If |subscription|'s subscription/top-level traversable ids set/contains |navigable|'s navigable id;
 1. set/Remove |navigable|'s navigable id from |subscription|'s subscription/top-level traversable ids.
 1. If |subscription|'s subscription/top-level traversable ids is empty:
 1. set/Append |subscription| to |subscriptions to remove|.
 1. list/Remove |subscriptions to remove| from |session|'s subscriptions.
Issue: It's unclear if we ought to only fire this event for browsing
contexts that have active documents; navigation can also cause contexts to
become inaccessible but not yet get discarded because bfcache.

```cddl
browsingContext.ContextDestroyed = (
         method: "browsingContext.contextDestroyed",
         params: browsingContext.Info
        )
```


#### 2.3.4.3. #### The browsingContext.navigationStarted Event ####

The remote end event trigger is the WebDriver BiDi navigation started steps
given /navigable |navigable| and WebDriver BiDi navigation status|navigation status
|navigation status|:
1. Let |params| be the result of get the navigation info given |navigable|
and |navigation status|.
 1. Let |body| be a /map matching the
browsingContext.NavigationStarted production, with the
params field set to |params|.
1. Let |navigation id| be |navigation status|'s WebDriver BiDi navigation status/id.
1. Let |related navigables| be a /set containing |navigable|.
1. Resume with "navigation started", |navigation id|, and
|navigation status|.
1. For each |session| in the set of sessions for which an event is enabled
given "browsingContext.navigationStarted" and |related navigables|:
 1. Emit an event with |session| and |body|.

```cddl
browsingContext.NavigationStarted = (
         method: "browsingContext.navigationStarted",
         params: browsingContext.NavigationInfo
        )
```


#### 2.3.4.4. #### The browsingContext.fragmentNavigated Event ####

The remote end event trigger is the WebDriver BiDi fragment navigated steps
given /navigable |navigable| and WebDriver BiDi navigation status|navigation status
|navigation status|:
1. Let |params| be the result of get the navigation info given |navigable|
and |navigation status|.
1. Let |body| be a /map matching the
browsingContext.FragmentNavigated production, with the
params field set to |params|.
1. Let |navigation id| be |navigation status|'s WebDriver BiDi navigation status/id.
1. Let |related navigable| be a /set containing |navigable|.
1. Resume with "fragment navigated", |navigation id|, and
|navigation status|.
1. For each |session| in the set of sessions for which an event is enabled
given "browsingContext.fragmentNavigated" and |related navigable|:
 1. Emit an event with |session| and |body|.

```cddl
browsingContext.FragmentNavigated = (
         method: "browsingContext.fragmentNavigated",
         params: browsingContext.NavigationInfo
        )
```


#### 2.3.4.5. #### The browsingContext.historyUpdated Event ####

browsingContext.HistoryUpdatedParameters = {
 context: browsingContext.BrowsingContext,
 timestamp: js-uint,
 url: text,
 ? userContext: browser.UserContext
 }

```cddl
browsingContext.HistoryUpdated = (
          method: "browsingContext.historyUpdated",
          params: browsingContext.HistoryUpdatedParameters
        )

        browsingContext.HistoryUpdatedParameters = {
          context: browsingContext.BrowsingContext,
          timestamp: js-uint,
          url: text,
          ? userContext: browser.UserContext
        }
```


#### 2.3.4.6. #### The browsingContext.domContentLoaded Event ####

The remote end event trigger is the WebDriver BiDi DOM content loaded steps
given /navigable |navigable| and WebDriver BiDi navigation status|navigation status
|navigation status|:
1. Let |params| be the result of get the navigation info given |navigable|
and |navigation status|.
1. Let |body| be a /map matching the
browsingContext.DomContentLoaded production, with the
params field set to |params|.
1. Let |related navigables| be a /set containing |navigable|.
1. Let |navigation id| be |navigation status|'s WebDriver BiDi navigation status/id.
1. Resume with "domContentLoaded", |navigation id|, and
|navigation status|.
1. For each |session| in the set of sessions for which an event is enabled
given "browsingContext.domContentLoaded" and |related navigables|:
 1. Emit an event with |session| and |body|.

```cddl
browsingContext.DomContentLoaded = (
         method: "browsingContext.domContentLoaded",
         params: browsingContext.NavigationInfo
        )
```


#### 2.3.4.7. #### The browsingContext.load Event ####

The remote end event trigger is the WebDriver BiDi load complete steps given
/navigable |navigable| and WebDriver BiDi navigation status|navigation status
|navigation status|:
1. Let |params| be the result of get the navigation info given |navigable|
and |navigation status|.
1. Let |body| be a /map matching the browsingContext.Load
production, with the params field set to |params|.
1. Let |related navigables| be a /set containing |navigable|.
1. Let |navigation id| be |navigation status|'s WebDriver BiDi navigation status/id.
1. Resume with "load", |navigation id| and
|navigation status|.
1. For each |session| in the set of sessions for which an event is enabled
given "browsingContext.load" and |related navigables|:
 1. Emit an event with |session| and |body|.

```cddl
browsingContext.Load = (
         method: "browsingContext.load",
         params: browsingContext.NavigationInfo
        )
```


#### 2.3.4.8. #### The browsingContext.downloadWillBegin Event ####

browsingContext.DownloadWillBeginParams = {
 download: browsingContext.Download,
 suggestedFilename: text,
 browsingContext.BaseNavigationInfo
 }

```cddl
browsingContext.DownloadWillBegin = (
         method: "browsingContext.downloadWillBegin",
         params: browsingContext.DownloadWillBeginParams
        )

        browsingContext.DownloadWillBeginParams = {
          download: browsingContext.Download,
          suggestedFilename: text,
          browsingContext.BaseNavigationInfo
        }
```


#### 2.3.4.9. #### The browsingContext.downloadEnd Event ####

browsingContext.DownloadEndParams = {
 (
 browsingContext.DownloadCanceledParams //
 browsingContext.DownloadCompleteParams
 )
 }

```cddl
browsingContext.DownloadEnd = (
          method: "browsingContext.downloadEnd",
          params: browsingContext.DownloadEndParams
        )

        browsingContext.DownloadEndParams = {
          (
            browsingContext.DownloadCanceledParams //
            browsingContext.DownloadCompleteParams
          )
        }

        browsingContext.DownloadCanceledParams = (
          status: "canceled",
          download: browsingContext.Download,
          browsingContext.BaseNavigationInfo
        )

        browsingContext.DownloadCompleteParams = (
          status: "complete",
          download: browsingContext.Download,
          filepath: text / null,
          browsingContext.BaseNavigationInfo
        )
```


#### 2.3.4.10. #### The browsingContext.navigationAborted Event ####

The remote end event trigger is the WebDriver BiDi navigation aborted steps
given /navigable |navigable| and WebDriver BiDi navigation status|navigation status
|navigation status|:
1. Let |params| be the result of get the navigation info given |navigable|
and |navigation status|.
1. Let |body| be a /map matching the
browsingContext.NavigationAborted production, with the
params field set to |params|.
1. Let |navigation id| be |navigation status|'s WebDriver BiDi navigation status/id.
1. Let |related navigables| be a /set containing |navigable|.
1. Resume with "navigation aborted", |navigation id|, and |navigation status|.
1. For each |session| in the set of sessions for which an event is enabled
given "browsingContext.navigationAborted" and |related navigables|:
 1. Emit an event with |session| and |body|.

```cddl
browsingContext.NavigationAborted = (
         method: "browsingContext.navigationAborted",
         params: browsingContext.NavigationInfo
        )
```


#### 2.3.4.11. #### The browsingContext.navigationCommitted Event ####

The remote end event trigger is the WebDriver BiDi navigation committed steps
given /navigable |navigable| and WebDriver BiDi navigation status|navigation status
|navigation status|:
1. Let |params| be the result of get the navigation info given |navigable|
and |navigation status|.
1. Let |body| be a /map matching the
browsingContext.NavigationCommitted production, with the
params field set to |params|.
1. Let |related navigables| be a /set containing |navigable|.
1. Let |navigation id| be |navigation status|'s WebDriver BiDi navigation status/id.
1. Resume with "navigation committed", |navigation id|, and |navigation status|.
1. For each |session| in the set of sessions for which an event is enabled
given "browsingContext.navigationCommitted" and |related navigables|:
 1. Emit an event with |session| and |body|.

```cddl
browsingContext.NavigationCommitted = (
         method: "browsingContext.navigationCommitted",
         params: browsingContext.NavigationInfo
        )
```


#### 2.3.4.12. #### The browsingContext.navigationFailed Event ####

The remote end event trigger is the WebDriver BiDi navigation failed steps
given /navigable |navigable| and WebDriver BiDi navigation status|navigation status
|navigation status|:
1. Let |params| be the result of get the navigation info given |navigable|
and |navigation status|.
1. Let |body| be a /map matching the
browsingContext.NavigationFailed production, with the
params field set to |params|.
1. Let |navigation id| be |navigation status|'s WebDriver BiDi navigation status/id.
1. Let |related navigables| be a /set containing |navigable|.
1. Resume with "navigation failed", |navigation id|, and |navigation status|.
1. For each |session| in the set of sessions for which an event is enabled
given "browsingContext.navigationFailed" and |related navigables|:
 1. Emit an event with |session| and |body|.

```cddl
browsingContext.NavigationFailed = (
         method: "browsingContext.navigationFailed",
         params: browsingContext.NavigationInfo
        )
```


#### 2.3.4.13. #### The browsingContext.userPromptClosed Event ####

browsingContext.UserPromptClosedParameters = {
 context: browsingContext.BrowsingContext,
 accepted: bool,
 type: browsingContext.UserPromptType,
 ? userContext: browser.UserContext,
 ? userText: text
 }

```cddl
browsingContext.UserPromptClosed = (
          method: "browsingContext.userPromptClosed",
          params: browsingContext.UserPromptClosedParameters
        )

        browsingContext.UserPromptClosedParameters = {
          context: browsingContext.BrowsingContext,
          accepted: bool,
          type: browsingContext.UserPromptType,
          ? userContext: browser.UserContext,
          ? userText: text
        }
```


#### 2.3.4.14. #### The browsingContext.userPromptOpened Event ####

browsingContext.UserPromptOpenedParameters = {
 context: browsingContext.BrowsingContext,
 handler: session.UserPromptHandlerType,
 message: text,
 type: browsingContext.UserPromptType,
 ? userContext: browser.UserContext,
 ? defaultValue: text
 }

```cddl
browsingContext.UserPromptOpened = (
          method: "browsingContext.userPromptOpened",
          params: browsingContext.UserPromptOpenedParameters
        )

        browsingContext.UserPromptOpenedParameters = {
          context: browsingContext.BrowsingContext,
          handler: session.UserPromptHandlerType,
          message: text,
          type: browsingContext.UserPromptType,
          ? userContext: browser.UserContext,
          ? defaultValue: text
        }
```


## 2.4. ## The emulation Module ##

The emulation module contains commands and events
relating to emulation of browser APIs.


### 2.4.1. ### Definition ###

A BiDi session has an emulated user agent which is a
struct with an struct/item named
default user agent, which is a string or null,
an struct/item named
user context user agent, which is a weak map
between user context|user contexts and string, and an struct/item named
navigable user agent, which is a weak map
between /navigables and string.

```cddl
EmulationCommand = (
  emulation.SetForcedColorsModeThemeOverride //
  emulation.SetGeolocationOverride //
  emulation.SetLocaleOverride //
  emulation.SetMediaFeaturesOverride //
  emulation.SetNetworkConditions //
  emulation.SetScreenOrientationOverride //
  emulation.SetScreenSettingsOverride //
  emulation.SetScriptingEnabled //
  emulation.SetScrollbarTypeOverride //
  emulation.SetTimezoneOverride //
  emulation.SetTouchOverride //
  emulation.SetUserAgentOverride //
  emulation.SetViewportMetaOverride
)
```

```cddl
EmulationResult = (
  emulation.SetForcedColorsModeThemeOverrideResult /
  emulation.SetGeolocationOverrideResult /
  emulation.SetLocaleOverrideResult /
  emulation.SetMediaFeaturesOverrideResult /
  emulation.SetScreenOrientationOverrideResult /
  emulation.SetScriptingEnabledResult /
  emulation.SetScrollbarTypeOverrideResult /
  emulation.SetTimezoneOverrideResult /
  emulation.SetTouchOverrideResult /
  emulation.SetUserAgentOverrideResult /
  emulation.SetViewportMetaOverrideResult
)
```


#### 2.4.2.1. #### The emulation.setForcedColorsModeThemeOverride Command ####

The emulation.setForcedColorsModeThemeOverride command modifies
forced colors mode theming characteristics on the given top-level traversables or user contexts.

> [!NOTE]
> Check out the ForcedColorsModeAutomationTheme for the corresponding enum mapping in the CSS specification.

```cddl
emulation.SetForcedColorsModeThemeOverride = (
        method: "emulation.setForcedColorsModeThemeOverride",
        params: emulation.SetForcedColorsModeThemeOverrideParameters
      )

      emulation.SetForcedColorsModeThemeOverrideParameters = {
        theme: emulation.ForcedColorsModeTheme / null,
        ? contexts: [+browsingContext.BrowsingContext],
        ? userContexts: [+browser.UserContext],
      }

      emulation.ForcedColorsModeTheme = "light" / "dark"
```

```cddl
emulation.SetForcedColorsModeThemeOverrideResult = EmptyResult
```


#### 2.4.2.2. #### The emulation.setGeolocationOverride Command ####

The emulation.setGeolocationOverride command modifies geolocation characteristics on the given top-level traversables or user contexts.

```cddl
emulation.SetGeolocationOverride = (
        method: "emulation.setGeolocationOverride",
        params: emulation.SetGeolocationOverrideParameters
      )

      emulation.SetGeolocationOverrideParameters = {
        (
          (coordinates: emulation.GeolocationCoordinates / null) //
          (error: emulation.GeolocationPositionError)
        ),
        ? contexts: [+browsingContext.BrowsingContext],
        ? userContexts: [+browser.UserContext],
      }

      emulation.GeolocationCoordinates = {
         latitude: -90.0..90.0,
         longitude: -180.0..180.0,
         ? accuracy: (float .ge 0.0) .default 1.0,
         ? altitude: float / null .default null,
         ? altitudeAccuracy: (float .ge 0.0) / null .default null,
         ? heading: (0.0...360.0) / null .default null,
         ? speed: (float .ge 0.0) / null .default null,
      }

      emulation.GeolocationPositionError = {
         type: "positionUnavailable"
      }
```

```cddl
emulation.SetGeolocationOverrideResult = EmptyResult
```


#### 2.4.2.3. #### The emulation.setLocaleOverride Command ####

The emulation.setLocaleOverride command modifies
locale on the given top-level traversables or user contexts.

```cddl
emulation.SetLocaleOverride = (
        method: "emulation.setLocaleOverride",
        params: emulation.SetLocaleOverrideParameters
      )

      emulation.SetLocaleOverrideParameters = {
        locale: text / null,
        ? contexts: [+browsingContext.BrowsingContext],
        ? userContexts: [+browser.UserContext],
      }
```

```cddl
emulation.SetLocaleOverrideResult = EmptyResult
```


#### 2.4.2.4. #### The emulation.setMediaFeaturesOverride Command ####

The emulation.setMediaFeaturesOverride command
allows overriding the values of various media features.

```cddl
emulation.SetMediaFeaturesOverride = (
        method: "emulation.setMediaFeaturesOverride",
        params: emulation.SetMediaFeaturesOverrideParameters
      )

      emulation.SetMediaFeaturesOverrideParameters = {
        features: emulation.MediaFeatures / null,
        ? contexts: [+browsingContext.BrowsingContext],
        ? userContexts: [+browser.UserContext],
      }

      emulation.MediaFeatures = [emulation.MediaFeature]

      emulation.MediaFeature = {
         name: text
         value: text
      }
```

```cddl
emulation.SetMediaFeaturesOverrideResult = EmptyResult
```


#### 2.4.2.5. #### The emulation.setNetworkConditions Command ####

The emulation.setNetworkConditions command
emulates specific network conditions for the given browsing context or for a user
context.

```cddl
emulation.SetNetworkConditions = (
        method: "emulation.setNetworkConditions",
        params: emulation.SetNetworkConditionsParameters
      )

      emulation.SetNetworkConditionsParameters = {
        networkConditions: emulation.NetworkConditions / null,
        ? contexts: [+browsingContext.BrowsingContext],
        ? userContexts: [+browser.UserContext],
      }

      emulation.NetworkConditions = emulation.NetworkConditionsOffline

      emulation.NetworkConditionsOffline = {
        type: "offline"
      }
```

```cddl
emulation.SetNetworkConditionsResult = EmptyResult
```


#### 2.4.2.6. #### The emulation.setScreenSettingsOverride Command ####

The emulation.setScreenSettingsOverride command
emulates web-exposed screen area and web-exposed available screen area of the given top-level traversables or user contexts.

```cddl
emulation.SetScreenSettingsOverride = (
        method: "emulation.setScreenSettingsOverride",
        params: emulation.SetScreenSettingsOverrideParameters
      )

      emulation.ScreenArea = {
        width: js-uint,
        height: js-uint
      }

      emulation.SetScreenSettingsOverrideParameters = {
        screenArea: emulation.ScreenArea / null,
        ? contexts: [+browsingContext.BrowsingContext],
        ? userContexts: [+browser.UserContext],
      }
```

```cddl
emulation.SetScreenSettingsOverrideResult = EmptyResult
```


#### 2.4.2.7. #### The emulation.setScreenOrientationOverride Command ####

The emulation.setScreenOrientationOverride command
emulates screen orientation of the given top-level traversables or user contexts.

```cddl
emulation.SetScreenOrientationOverride = (
        method: "emulation.setScreenOrientationOverride",
        params: emulation.SetScreenOrientationOverrideParameters
      )

      emulation.ScreenOrientationNatural = "portrait" / "landscape"
      emulation.ScreenOrientationType = "portrait-primary" / "portrait-secondary" / "landscape-primary" / "landscape-secondary"

      emulation.ScreenOrientation = {
        natural: emulation.ScreenOrientationNatural,
        type: emulation.ScreenOrientationType
      }

      emulation.SetScreenOrientationOverrideParameters = {
        screenOrientation: emulation.ScreenOrientation / null,
        ? contexts: [+browsingContext.BrowsingContext],
        ? userContexts: [+browser.UserContext],
      }
```

```cddl
emulation.SetScreenOrientationOverrideResult = EmptyResult
```


#### 2.4.2.8. #### The emulation.setUserAgentOverride Command ####

The emulation.setUserAgentOverride command modifies
User-Agent on the given top-level traversables, user contexts, or globally.

```cddl
emulation.SetUserAgentOverride = (
        method: "emulation.setUserAgentOverride",
        params: emulation.SetUserAgentOverrideParameters
      )

      emulation.SetUserAgentOverrideParameters = {
        userAgent: text / null,
        ? contexts: [+browsingContext.BrowsingContext],
        ? userContexts: [+browser.UserContext],
      }
```

```cddl
emulation.SetUserAgentOverrideResult = EmptyResult
```


#### 2.4.2.9. #### The emulation.setViewportMetaOverride Command ####

The emulation.setViewportMetaOverride command modifies whether the browser respects
the &lt;meta name=viewport&gt; tag.

```cddl
emulation.SetViewportMetaOverride = (
        method: "emulation.setViewportMetaOverride",
        params: emulation.SetViewportMetaOverrideParameters
      )

      emulation.SetViewportMetaOverrideParameters = {
        viewportMeta: true / null,
        ? contexts: [+browsingContext.BrowsingContext],
        ? userContexts: [+browser.UserContext],
      }
```

```cddl
emulation.SetViewportMetaOverrideResult = EmptyResult
```


#### 2.4.2.10. #### The emulation.setScriptingEnabled Command ####

The emulation.setScriptingEnabled command emulates
disabling JavaScript on web pages.

> [!NOTE]
> only emulation of disabled Javascript is supported.

```cddl
emulation.SetScriptingEnabled = (
        method: "emulation.setScriptingEnabled",
        params: emulation.SetScriptingEnabledParameters
      )

      emulation.SetScriptingEnabledParameters = {
        enabled: false / null,
        ? contexts: [+browsingContext.BrowsingContext],
        ? userContexts: [+browser.UserContext],
      }
```

```cddl
emulation.SetScriptingEnabledResult = EmptyResult
```


#### 2.4.2.11. #### The emulation.setScrollbarTypeOverride Command ####

The emulation.setScrollbarTypeOverride command modifies
scrollbar type on the given top-level traversables, user contexts or globally.

```cddl
emulation.SetScrollbarTypeOverride = (
        method: "emulation.setScrollbarTypeOverride",
        params: emulation.SetScrollbarTypeOverrideParameters
      )

      emulation.SetScrollbarTypeOverrideParameters = {
        scrollbarType: "classic" / "overlay" / null,
        ? contexts: [+browsingContext.BrowsingContext],
        ? userContexts: [+browser.UserContext],
      }
```

```cddl
emulation.SetScrollbarTypeOverrideResult = EmptyResult
```


#### 2.4.2.12. #### The emulation.setTimezoneOverride Command ####

The emulation.setTimezoneOverride command modifies
timezone on the given top-level traversables or user contexts.

```cddl
emulation.SetTimezoneOverride = (
        method: "emulation.setTimezoneOverride",
        params: emulation.SetTimezoneOverrideParameters
      )

      emulation.SetTimezoneOverrideParameters = {
        timezone: text / null,
        ? contexts: [+browsingContext.BrowsingContext],
        ? userContexts: [+browser.UserContext],
      }
```

```cddl
emulation.SetTimezoneOverrideResult = EmptyResult
```


#### 2.4.2.13. #### The emulation.setTouchOverride Command ####

The emulation.setTouchOverride command emulates
enabled touch input on web pages.

```cddl
emulation.SetTouchOverride = (
        method: "emulation.setTouchOverride",
        params: emulation.SetTouchOverrideParameters
      )

      emulation.SetTouchOverrideParameters = {
        maxTouchPoints: (js-uint .ge 1) / null,
        ? contexts: [+browsingContext.BrowsingContext],
        ? userContexts: [+browser.UserContext],
      }
```

```cddl
emulation.SetTouchOverrideResult = EmptyResult
```


## 2.5. ## The network Module ##

The network module contains commands and events
relating to network requests.


### 2.5.1. ### Definition ###

NetworkCommand = (
 network.AddDataCollector //
 network.AddIntercept //
 network.ContinueRequest //
 network.ContinueResponse //
 network.ContinueWithAuth //
 network.DisownData //
 network.FailRequest //
 network.GetData //
 network.ProvideResponse //
 network.RemoveDataCollector //
 network.RemoveIntercept //
 network.SetCacheBehavior //
 network.SetExtraHeaders
)

```cddl
NetworkCommand = (
  network.AddDataCollector //
  network.AddIntercept //
  network.ContinueRequest //
  network.ContinueResponse //
  network.ContinueWithAuth //
  network.DisownData //
  network.FailRequest //
  network.GetData //
  network.ProvideResponse //
  network.RemoveDataCollector //
  network.RemoveIntercept //
  network.SetCacheBehavior //
  network.SetExtraHeaders
)
```

```cddl
NetworkResult = (
  network.AddDataCollectorResult /
  network.AddInterceptResult /
  network.ContinueRequestResult /
  network.ContinueResponseResult /
  network.ContinueWithAuthResult /
  network.DisownDataResult /
  network.FailRequestResult /
  network.GetDataResult /
  network.ProvideResponseResult /
  network.RemoveDataCollectorResult /
  network.RemoveInterceptResult /
  network.SetCacheBehaviorResult /
  network.SetExtraHeadersResult
)

NetworkEvent = (
    network.AuthRequired //
    network.BeforeRequestSent //
    network.FetchError //
    network.ResponseCompleted //
    network.ResponseStarted
)
```


#### 2.5.2.1. #### The network.AuthChallenge Type ####

**Algorithm: To extract challengesgiven |response|**
To extract challenges given |response|:
Issue: Should we include parameters other than realm?
1. If |response|'s response/status is 401, let |header name| be
`WWW-Authenticate`. Otherwise if |response|'s response/status is 407, let
|header name| be `Proxy-Authenticate`. Otherwise return null.
1. Let |challenges| be a new /list.
1. For each (|name|, |value|) in |response|'s response/header list:
Issue: as in Fetch it's unclear if this is the right way to handle multiple
headers, parsing issues, etc.
 1. If |name| is a byte-case-insensitive match for |header name|:
 1. Let |header challenges| be the result of parsing |value| into a list of
challenges, each consisting of a scheme and a list of parameters, each of
which is a tuple (name, value), according to the rules of [[!RFC9110]].
 1. For each |header challenge| in |header challenges|:
 1. Let |scheme| be |header challenge|'s scheme.
 1. Let |realm| be the empty string.
 1. For each (|param name|, |param value|) in |header challenge|'s
parameters:
 1. If |param name| equals `realm` let |realm| be
UTF-8 decode |param value|.
 1. Let |challenge| be a new /map matching the
network.AuthChallenge production, with the
scheme field set to |scheme| and the realm
field set to |realm|.
 1. list/Append |challenge| to |challenges|.
1. Return |challenges|.

```cddl
network.AuthChallenge = {
  scheme: text,
  realm: text,
}
```


#### 2.5.2.2. #### The network.AuthCredentials Type ####

The network.AuthCredentials type represents the response to a
request for authorization credentials.

```cddl
network.AuthCredentials = {
  type: "password",
  username: text,
  password: text,
}
```


#### 2.5.2.3. #### The network.BaseParameters Type ####

The network.BaseParameters type is an abstract type representing
the data that's common to all network events.

> [!IMPORTANT]
> Consider including the `sharedId` of the document node that initiated the
request in addition to the context.

```cddl
network.BaseParameters = (
    context: browsingContext.BrowsingContext / null,
    isBlocked: bool,
    navigation: browsingContext.Navigation / null,
    redirectCount: js-uint,
    request: network.RequestData,
    timestamp: js-uint,
    ? userContext: browser.UserContext / null,
    ? intercepts: [+network.Intercept]
)
```


#### 2.5.2.4. #### The network.BytesValue Type ####

network.StringValue = {
 type: "string",
 value: text,
}

```cddl
network.BytesValue = network.StringValue / network.Base64Value;

network.StringValue = {
  type: "string",
  value: text,
}

network.Base64Value = {
  type: "base64",
  value: text,
}
```


#### 2.5.2.5. #### The network.Collector Type ####

The network.Collector type represents the id of a network/collector.

```cddl
network.Collector = text
```


#### 2.5.2.6. #### The network.CollectorType Type ####

The network.CollectorType type represents the different types of data collectors
that can be added.

> [!NOTE]
> In the future we might also support the "stream" collector type for clients
which want to read the data gathered by a given collector via a stream.

```cddl
network.CollectorType = "blob"
```


#### 2.5.2.7. #### The network.Cookie Type ####

network.SameSite = "strict" / "lax" / "none" / "default"

```cddl
network.SameSite = "strict" / "lax" / "none" / "default"

<!--
Modifications to this definition should be reflected in
`network.SetCookieHeader`, `storage.CookieFilter`, and `storage.PartialCookie`.
-->
network.Cookie = {
    name: text,
    value: network.BytesValue,
    domain: text,
    path: text,
    size: js-uint,
    httpOnly: bool,
    secure: bool,
    sameSite: network.SameSite,
    ? expiry: js-uint,
    Extensible,
}
```


#### 2.5.2.8. #### The network.CookieHeader Type ####

The network.CookieHeader type represents the subset of cookie data
that's in a Cookie request header.

```cddl
network.CookieHeader = {
    name: text,
    value: network.BytesValue,
}
```


#### 2.5.2.9. #### The network.DataType Type ####

The network.DataType type represents the different types of network data
that can be collected.

```cddl
network.DataType = "request" / "response"
```


#### 2.5.2.10. #### The network.FetchTimingInfo Type ####

The network.FetchTimingInfo type represents the time of each part
of the request, relative to the time origin of the /request's
request/client.

```cddl
network.FetchTimingInfo = {
    timeOrigin: float,
    requestTime: float,
    redirectStart: float,
    redirectEnd: float,
    fetchStart: float,
    dnsStart: float,
    dnsEnd: float,
    connectStart: float,
    connectEnd: float,
    tlsStart: float,
    <!-- tlsEnd: float this should be the same as connectEnd -->
    requestStart: float,
    responseStart: float,
    <!-- TODO responseHeadersEnd: float: Not sure quite what to use for this -->
    responseEnd: float,
}
```


#### 2.5.2.11. #### The network.Header Type ####

The network.Header type represents a single request header.

```cddl
network.Header = {
  name: text,
  value: network.BytesValue,
}
```


#### 2.5.2.12. #### The network.Initiator Type ####

The network.Initiator type represents the source of a network
request.

> [!NOTE]
> The type field is included in the definition for backwards
compatibility, but is no longer set by the get the initiator steps, and will
be removed in a future revision of this specification. Its use is expected to be
replaced by initiatorType and destination on
network.RequestData.
> [!NOTE]
> The request field is included in the definition for backwards
compatibility, but is no longer set by the get the initiator steps, and will
be removed in a future revision of this specification. The
network.Initiator is included in the
network.BeforeRequestSentParameters which also contain the same
request id, making this information redundant. See
[[#type-network-BaseParameters]].

```cddl
network.Initiator = {
    ? columnNumber: js-uint,
    ? lineNumber: js-uint,
    ? request: network.Request,
    ? stackTrace: script.StackTrace,
    ? type: "parser" / "script" / "preflight" / "other"
}
```


#### 2.5.2.13. #### The network.Intercept Type ####

The network.Intercept type represents the id of a network intercept.

```cddl
network.Intercept = text
```


#### 2.5.2.14. #### The network.Request Type ####

Each network request has an associated request id, which is a
string uniquely identifying that request. The identifier for a request resulting from a
redirect matches that of the request that initiated it.

```cddl
network.Request = text;
```


#### 2.5.2.15. #### The network.RequestData Type ####

The network.RequestData type represents an ongoing network request.

```cddl
network.RequestData = {
    request: network.Request,
    url: text,
    method: text,
    headers: [*network.Header],
    cookies: [*network.Cookie],
    headersSize: js-uint,
    bodySize: js-uint / null,
    destination: text,
    initiatorType: text / null,
    timings: network.FetchTimingInfo,
}
```


#### 2.5.2.16. #### The network.ResponseContent Type ####

The network.ResponseContent type represents the decoded response to
a network request.

```cddl
network.ResponseContent = {
    size: js-uint
}
```


#### 2.5.2.17. #### The network.ResponseData Type ####

The network.ResponseData type represents the response to a network
request.

```cddl
network.ResponseData = {
    url: text,
    protocol: text,
    status: js-uint,
    statusText: text,
    fromCache: bool,
    headers: [*network.Header],
    mimeType: text,
    bytesReceived: js-uint,
    headersSize: js-uint / null,
    bodySize: js-uint / null,
    content: network.ResponseContent,
    ?authChallenges: [*network.AuthChallenge],
}
```


#### 2.5.2.18. #### The network.SetCookieHeader Type ####

The network.SetCookieHeader represents the data in a
Set-Cookie response header.

```cddl
<!--
Modifications to this definition should be reflected in
`network.Cookie`, `storage.CookieFilter`, and `storage.PartialCookie`.
-->
network.SetCookieHeader = {
    name: text,
    value: network.BytesValue,
    ? domain: text,
    ? httpOnly: bool,
    ? expiry: text,
    ? maxAge: js-int,
    ? path: text,
    ? sameSite: network.SameSite,
    ? secure: bool,
}
```


#### 2.5.2.19. #### The network.UrlPattern Type ####

network.UrlPatternPattern = {
 type: "pattern",
 ?protocol: text,
 ?hostname: text,
 ?port: text,
 ?pathname: text,
 ?search: text,
}

> [!NOTE]
> This syntax is designed with future extensibility in mind. In particular
the syntax forbids characters that are treated specially in the [[URLPattern]]
specification. These can be escaped by prefixing them with a U+005C (\) character.

```cddl
network.UrlPattern = (
  network.UrlPatternPattern /
  network.UrlPatternString
)

network.UrlPatternPattern = {
    type: "pattern",
    ?protocol: text,
    ?hostname: text,
    ?port: text,
    ?pathname: text,
    ?search: text,
}


network.UrlPatternString = {
    type: "string",
    pattern: text,
}
```


#### 2.5.3.1. #### The network.addDataCollector Command ####

The network.addDataCollector adds a
network/collector.

```cddl
network.AddDataCollector = (
        method: "network.addDataCollector",
        params: network.AddDataCollectorParameters
      )

      network.AddDataCollectorParameters = {
        dataTypes: [+network.DataType],
        maxEncodedDataSize: js-uint,
        ? collectorType: network.CollectorType .default "blob",
        ? contexts: [+browsingContext.BrowsingContext],
        ? userContexts: [+browser.UserContext],
      }
```

```cddl
network.AddDataCollectorResult = {
        collector: network.Collector
      }
```


#### 2.5.3.2. #### The network.addIntercept Command ####

The network.addIntercept command adds a
network intercept.

```cddl
network.AddIntercept = (
        method: "network.addIntercept",
        params: network.AddInterceptParameters
      )

      network.AddInterceptParameters = {
        phases: [+network.InterceptPhase],
        ? contexts: [+browsingContext.BrowsingContext],
        ? urlPatterns: [*network.UrlPattern],
      }

      network.InterceptPhase = "beforeRequestSent" / "responseStarted" /
                               "authRequired"
```

```cddl
network.AddInterceptResult = {
        intercept: network.Intercept
      }
```


#### 2.5.3.3. #### The network.continueRequest Command ####

The network.continueRequest command continues a request
that's blocked by a network intercept.

```cddl
network.ContinueRequest = (
        method: "network.continueRequest",
        params: network.ContinueRequestParameters
      )

      network.ContinueRequestParameters = {
        request: network.Request,
        ?body: network.BytesValue,
        ?cookies: [*network.CookieHeader],
        ?headers: [*network.Header],
        ?method: text,
        ?url: text,
      }
```

```cddl
network.ContinueRequestResult = EmptyResult
```


#### 2.5.3.4. #### The network.continueResponse Command ####

The network.continueResponse command continues a
response that's blocked by a network intercept. It can be called in the
responseStarted phase, to modify the status and headers of the
response, but still provide the network response body.

```cddl
network.ContinueResponse = (
        method: "network.continueResponse",
        params: network.ContinueResponseParameters
      )

      network.ContinueResponseParameters = {
        request: network.Request,
        ?cookies: [*network.SetCookieHeader]
        ?credentials: network.AuthCredentials,
        ?headers: [*network.Header],
        ?reasonPhrase: text,
        ?statusCode: js-uint,
      }
```

```cddl
network.ContinueResponseResult = EmptyResult
```


#### 2.5.3.5. #### The network.continueWithAuth Command ####

The network.continueWithAuth command continues a
response that's blocked by a network intercept at the
authRequired phase.

```cddl
network.ContinueWithAuth = (
        method: "network.continueWithAuth",
        params: network.ContinueWithAuthParameters
      )

      network.ContinueWithAuthParameters = {
        request: network.Request,
        (network.ContinueWithAuthCredentials // network.ContinueWithAuthNoCredentials)
      }

      network.ContinueWithAuthCredentials = (
        action: "provideCredentials", <!-- or "provide credentials" or
      "providecredentials" or something else -->
        credentials: network.AuthCredentials
      )

      network.ContinueWithAuthNoCredentials = (
        action: "default" / "cancel"
      )
```

```cddl
network.ContinueWithAuthResult = EmptyResult
```


#### 2.5.3.6. #### The network.disownData Command ####

The network.disownData command releases a
collected network data for a given network/collector.

```cddl
network.DisownData = (
        method: "network.disownData",
        params: network.DisownDataParameters
      )

      network.DisownDataParameters = {
        dataType: network.DataType,
        collector: network.Collector,
        request: network.Request,
      }
```

```cddl
network.DisownDataResult = EmptyResult
```


#### 2.5.3.7. #### The network.failRequest Command ####

The network.failRequest command fails a
fetch that's blocked by a network intercept.

```cddl
network.FailRequest = (
        method: "network.failRequest",
        params: network.FailRequestParameters
      )

      network.FailRequestParameters = {
        request: network.Request,
      }
```

```cddl
network.FailRequestResult = EmptyResult
```


#### 2.5.3.8. #### The network.getData Command ####

The network.getData command retrieves a
network data if it is available.

```cddl
network.GetData = (
        method: "network.getData",
        params: network.GetDataParameters
      )

      network.GetDataParameters = {
        dataType: network.DataType,
        ? collector: network.Collector,
        ? disown: bool .default false,
        request: network.Request,
      }
```

```cddl
network.GetDataResult = {
        bytes: network.BytesValue,
      }
```


#### 2.5.3.9. #### The network.provideResponse Command ####

The network.provideResponse command continues a
request that's blocked by a network intercept, by providing a complete
response.

> [!NOTE]
> This will not prevent the request going through the normal request
lifecycle, and therefore emitting other events as it progresses.

```cddl
network.ProvideResponse = (
        method: "network.provideResponse",
        params: network.ProvideResponseParameters
      )

      network.ProvideResponseParameters = {
        request: network.Request,
        ?body: network.BytesValue,
        ?cookies: [*network.SetCookieHeader],
        ?headers: [*network.Header],
        ?reasonPhrase: text,
        ?statusCode: js-uint,
      }
```

```cddl
network.ProvideResponseResult = EmptyResult
```


#### 2.5.3.10. #### The network.removeDataCollector Command ####

The network.removeDataCollector command removes a
network/collector.

```cddl
network.RemoveDataCollector = (
        method: "network.removeDataCollector",
        params: network.RemoveDataCollectorParameters
      )

      network.RemoveDataCollectorParameters = {
        collector: network.Collector
      }
```

```cddl
network.RemoveDataCollectorResult = EmptyResult
```


#### 2.5.3.11. #### The network.removeIntercept Command ####

The network.removeIntercept command removes a
network intercept.

```cddl
network.RemoveIntercept = (
        method: "network.removeIntercept",
        params: network.RemoveInterceptParameters
      )

      network.RemoveInterceptParameters = {
        intercept: network.Intercept
      }
```

```cddl
network.RemoveInterceptResult = EmptyResult
```


#### 2.5.3.12. #### The network.setCacheBehavior Command ####

The network.setCacheBehavior command configures
the network cache behavior for certain requests.

```cddl
network.SetCacheBehavior = (
        method: "network.setCacheBehavior",
        params: network.SetCacheBehaviorParameters
      )

      network.SetCacheBehaviorParameters = {
        cacheBehavior: "default" / "bypass",
        ? contexts: [+browsingContext.BrowsingContext]
      }
```

```cddl
network.SetCacheBehaviorResult = EmptyResult
```


#### 2.5.3.13. #### The network.setExtraHeaders Command ####

The network.setExtraHeaders command allows
specifying headers that will extend, or overwrite, existing request headers.

```cddl
network.SetExtraHeaders = (
        method: "network.setExtraHeaders",
        params: network.SetExtraHeadersParameters
      )

      network.SetExtraHeadersParameters = {
        headers: [*network.Header]
        ? contexts: [+browsingContext.BrowsingContext]
        ? userContexts: [+browser.UserContext]
      }
```

```cddl
network.SetExtraHeadersResult = EmptyResult
```


#### 2.5.4.1. #### The network.authRequired Event ####

network.AuthRequiredParameters = {
 network.BaseParameters,
 response: network.ResponseData
 }

```cddl
network.AuthRequired = (
        method: "network.authRequired",
        params: network.AuthRequiredParameters
      )

      network.AuthRequiredParameters = {
        network.BaseParameters,
        response: network.ResponseData
      }
```


#### 2.5.4.2. #### The network.beforeRequestSent Event ####

network.BeforeRequestSentParameters = {
 network.BaseParameters,
 ? initiator: network.Initiator,
 }

```cddl
network.BeforeRequestSent = (
         method: "network.beforeRequestSent",
         params: network.BeforeRequestSentParameters
        )

       network.BeforeRequestSentParameters = {
         network.BaseParameters,
         ? initiator: network.Initiator,
       }
```


#### 2.5.4.3. #### The network.fetchError Event ####

network.FetchErrorParameters = {
 network.BaseParameters,
 errorText: text,
 }

```cddl
network.FetchError = (
         method: "network.fetchError",
         params: network.FetchErrorParameters
        )

       network.FetchErrorParameters = {
         network.BaseParameters,
         errorText: text,
       }
```


#### 2.5.4.4. #### The network.responseCompleted Event ####

network.ResponseCompletedParameters = {
 network.BaseParameters,
 response: network.ResponseData,
 }

```cddl
network.ResponseCompleted = (
         method: "network.responseCompleted",
         params: network.ResponseCompletedParameters
        )

       network.ResponseCompletedParameters = {
         network.BaseParameters,
         response: network.ResponseData,
       }
```


#### 2.5.4.5. #### The network.responseStarted Event ####

network.ResponseStartedParameters = {
 network.BaseParameters,
 response: network.ResponseData,
 }

```cddl
network.ResponseStarted = (
         method: "network.responseStarted",
         params: network.ResponseStartedParameters
        )

       network.ResponseStartedParameters = {
         network.BaseParameters,
         response: network.ResponseData,
       }
```


## 2.6. ## The script Module ##

The script module contains commands and events
relating to script realms and execution.


### 2.6.1. ### Definition ###

ScriptEvent = (
 script.Message //
 script.RealmCreated //
 script.RealmDestroyed
)

```cddl
ScriptCommand = (
  script.AddPreloadScript //
  script.CallFunction //
  script.Disown //
  script.Evaluate //
  script.GetRealms //
  script.RemovePreloadScript
)
```

```cddl
ScriptResult = (
  script.AddPreloadScriptResult /
  script.CallFunctionResult /
  script.DisownResult /
  script.EvaluateResult /
  script.GetRealmsResult /
  script.RemovePreloadScriptResult
)

ScriptEvent = (
  script.Message //
  script.RealmCreated //
  script.RealmDestroyed
)
```


#### 2.6.2.1. #### The script.Channel Type ####

The script.Channel type represents the id of a specific channel
used to send custom messages from the remote end to the local end.

```cddl
script.Channel = text;
```


#### 2.6.2.2. #### The script.ChannelValue Type ####

script.ChannelProperties = {
 channel: script.Channel,
 ? serializationOptions: script.SerializationOptions,
 ? ownership: script.ResultOwnership,
}

```cddl
script.ChannelValue = {
  type: "channel",
  value: script.ChannelProperties,
}

script.ChannelProperties = {
  channel: script.Channel,
  ? serializationOptions: script.SerializationOptions,
  ? ownership: script.ResultOwnership,
}
```


#### 2.6.2.3. #### The script.EvaluateResult Type ####

script.EvaluateResultSuccess = {
 type: "success",
 result: script.RemoteValue,
 realm: script.Realm
}

```cddl
script.EvaluateResult = (
  script.EvaluateResultSuccess /
  script.EvaluateResultException
)

script.EvaluateResultSuccess = {
  type: "success",
  result: script.RemoteValue,
  realm: script.Realm
}

script.EvaluateResultException = {
  type: "exception",
  exceptionDetails: script.ExceptionDetails
  realm: script.Realm
}
```


#### 2.6.2.4. #### The script.ExceptionDetails Type ####

The script.ExceptionDetails type represents a JavaScript exception.

```cddl
script.ExceptionDetails = {
  columnNumber: js-uint,
  exception: script.RemoteValue,
  lineNumber: js-uint,
  stackTrace: script.StackTrace,
  text: text,
}
```


#### 2.6.2.5. #### The script.Handle Type ####

The script.Handle type represents a handle to an object owned by
the ECMAScript runtime. The handle is only valid in a specific Realm.

```cddl
script.Handle = text;
```


#### 2.6.2.6. #### The script.InternalId Type ####

The script.InternalId type represents the id of
a previously serialized script.RemoteValue during
serialize as a remote value|serialization.

```cddl
script.InternalId = text;
```


#### 2.6.2.7. #### The script.LocalValue Type ####

script.ListLocalValue = [*script.LocalValue];

```cddl
script.LocalValue = (
  script.RemoteReference /
  script.PrimitiveProtocolValue /
  script.ChannelValue /
  script.ArrayLocalValue /
  { script.DateLocalValue } /
  script.MapLocalValue /
  script.ObjectLocalValue /
  { script.RegExpLocalValue } /
  script.SetLocalValue
)

script.ListLocalValue = [*script.LocalValue];

script.ArrayLocalValue = {
  type: "array",
  value: script.ListLocalValue,
}

script.DateLocalValue = (
  type: "date",
  value: text
)

script.MappingLocalValue = [*[(script.LocalValue / text), script.LocalValue]];

script.MapLocalValue = {
  type: "map",
  value: script.MappingLocalValue,
}

script.ObjectLocalValue = {
  type: "object",
  value: script.MappingLocalValue,
}

script.RegExpValue = {
  pattern: text,
  ? flags: text,
}

script.RegExpLocalValue = (
  type: "regexp",
  value: script.RegExpValue,
)

script.SetLocalValue = {
  type: "set",
  value: script.ListLocalValue,
}
```


#### 2.6.2.8. #### The script.PreloadScript Type ####

The script.PreloadScript type represents a handle to a script that will run
on realm creation.

```cddl
script.PreloadScript = text;
```


#### 2.6.2.9. #### The script.Realm Type ####

Each realm has an associated realm id, which is a string
uniquely identifying that realm. This is implicitly set when the realm is
created.

> [!NOTE]
> this is to ensure that users do not rely on implementation-specific
relationships between different ids.

```cddl
script.Realm = text;
```


#### 2.6.2.10. #### The script.PrimitiveProtocolValue Type ####

script.UndefinedValue = {
 type: "undefined",
}

```cddl
script.PrimitiveProtocolValue = (
  script.UndefinedValue /
  script.NullValue /
  script.StringValue /
  script.NumberValue /
  script.BooleanValue /
  script.BigIntValue
)

script.UndefinedValue = {
  type: "undefined",
}

script.NullValue = {
  type: "null",
}

script.StringValue = {
  type: "string",
  value: text,
}

script.SpecialNumber = "NaN" / "-0" / "Infinity" / "-Infinity";

script.NumberValue = {
  type: "number",
  value: number / script.SpecialNumber,
}

script.BooleanValue = {
  type: "boolean",
  value: bool,
}

script.BigIntValue = {
  type: "bigint",
  value: text,
}
```


#### 2.6.2.11. #### The script.RealmInfo Type ####

script.BaseRealmInfo = (
 realm: script.Realm,
 origin: text
)

> [!NOTE]
> there's a 1:1 relationship between the script.RealmInfo
 variants and values of script.RealmType.

```cddl
script.RealmInfo = (
  script.WindowRealmInfo /
  script.DedicatedWorkerRealmInfo /
  script.SharedWorkerRealmInfo /
  script.ServiceWorkerRealmInfo /
  script.WorkerRealmInfo /
  script.PaintWorkletRealmInfo /
  script.AudioWorkletRealmInfo /
  script.WorkletRealmInfo
)

script.BaseRealmInfo = (
  realm: script.Realm,
  origin: text
)

script.WindowRealmInfo = {
  script.BaseRealmInfo,
  type: "window",
  context: browsingContext.BrowsingContext,
  ? userContext: browser.UserContext,
  ? sandbox: text
}

script.DedicatedWorkerRealmInfo = {
  script.BaseRealmInfo,
  type: "dedicated-worker",
  owners: [script.Realm]
}

script.SharedWorkerRealmInfo = {
  script.BaseRealmInfo,
  type: "shared-worker"
}

script.ServiceWorkerRealmInfo = {
  script.BaseRealmInfo,
  type: "service-worker"
}

script.WorkerRealmInfo = {
  script.BaseRealmInfo,
  type: "worker"
}

script.PaintWorkletRealmInfo = {
  script.BaseRealmInfo,
  type: "paint-worklet"
}

script.AudioWorkletRealmInfo = {
  script.BaseRealmInfo,
  type: "audio-worklet"
}

script.WorkletRealmInfo = {
  script.BaseRealmInfo,
  type: "worklet"
}
```


#### 2.6.2.12. #### The script.RealmType Type ####

The script.RealmType type represents the different types of Realm.

```cddl
script.RealmType = "window" / "dedicated-worker" / "shared-worker" / "service-worker" /
                   "worker" / "paint-worklet" / "audio-worklet" / "worklet"
```


#### 2.6.2.13. #### The script.RemoteReference Type ####

script.SharedReference = {
 sharedId: script.SharedId
 
 ? handle: script.Handle,
 Extensible
}

> [!IMPORTANT]
> handle "stale object reference" case.
> [!NOTE]
> if the provided reference has both handle and
sharedId, the algorithm will ignore handle and respect
only sharedId.

```cddl
<!-- This is specifically ordered in the order in which matches need to be -->
<!-- evaluated, since the definitions are overlapping -->
script.RemoteReference = (
  script.SharedReference /
  script.RemoteObjectReference
)

script.SharedReference = {
   sharedId: script.SharedId
   <!-- Ensure that if we have a handle, it at least has the correct type -->
   ? handle: script.Handle,
   Extensible
}

script.RemoteObjectReference = {
   handle: script.Handle,
   <!-- This shouldn't ever match. The problem is that Extensible would
   otherwise allow this to match a non-text sharedId -->
   ? sharedId: script.SharedId
   Extensible
}
```


#### 2.6.2.14. #### The script.RemoteValue Type ####

script.ListRemoteValue = [*script.RemoteValue];

> [!IMPORTANT]
> Add WASM types?
> [!IMPORTANT]
> Should WindowProxy get attributes in a similar style to Node?
> [!IMPORTANT]
> handle String / Number / etc. wrapper objects specially?
> [!IMPORTANT]
> reconsider mirror objects' lifecycle.
> [!NOTE]
> mirror objects do not keep the original object alive in the runtime. If an
object is discarded in the runtime, subsequent attempts to access it via the
protocol will result in an error.

```cddl
script.RemoteValue = (
  script.PrimitiveProtocolValue /
  script.SymbolRemoteValue /
  script.ArrayRemoteValue /
  script.ObjectRemoteValue /
  script.FunctionRemoteValue /
  script.RegExpRemoteValue /
  script.DateRemoteValue /
  script.MapRemoteValue /
  script.SetRemoteValue /
  script.WeakMapRemoteValue /
  script.WeakSetRemoteValue /
  script.GeneratorRemoteValue /
  script.ErrorRemoteValue /
  script.ProxyRemoteValue /
  script.PromiseRemoteValue /
  script.TypedArrayRemoteValue /
  script.ArrayBufferRemoteValue /
  script.NodeListRemoteValue /
  script.HTMLCollectionRemoteValue /
  script.NodeRemoteValue /
  script.WindowProxyRemoteValue
)

script.ListRemoteValue = [*script.RemoteValue];

script.MappingRemoteValue = [*[(script.RemoteValue / text), script.RemoteValue]];

script.SymbolRemoteValue = {
  type: "symbol",
  ? handle: script.Handle,
  ? internalId: script.InternalId,
}

script.ArrayRemoteValue = {
  type: "array",
  ? handle: script.Handle,
  ? internalId: script.InternalId,
  ? value: script.ListRemoteValue,
}

script.ObjectRemoteValue = {
  type: "object",
  ? handle: script.Handle,
  ? internalId: script.InternalId,
  ? value: script.MappingRemoteValue,
}

script.FunctionRemoteValue = {
  type: "function",
  ? handle: script.Handle,
  ? internalId: script.InternalId,
}

script.RegExpRemoteValue = {
  script.RegExpLocalValue,
  ? handle: script.Handle,
  ? internalId: script.InternalId,
}

script.DateRemoteValue = {
  script.DateLocalValue,
  ? handle: script.Handle,
  ? internalId: script.InternalId,
}

script.MapRemoteValue = {
  type: "map",
  ? handle: script.Handle,
  ? internalId: script.InternalId,
  ? value: script.MappingRemoteValue,
}

script.SetRemoteValue = {
  type: "set",
  ? handle: script.Handle,
  ? internalId: script.InternalId,
  ? value: script.ListRemoteValue
}

script.WeakMapRemoteValue = {
  type: "weakmap",
  ? handle: script.Handle,
  ? internalId: script.InternalId,
}

script.WeakSetRemoteValue = {
  type: "weakset",
  ? handle: script.Handle,
  ? internalId: script.InternalId,
}

script.GeneratorRemoteValue = {
  type: "generator",
  ? handle: script.Handle,
  ? internalId: script.InternalId,
}

script.ErrorRemoteValue = {
  type: "error",
  ? handle: script.Handle,
  ? internalId: script.InternalId,
}

script.ProxyRemoteValue = {
  type: "proxy",
  ? handle: script.Handle,
  ? internalId: script.InternalId,
}

script.PromiseRemoteValue = {
  type: "promise",
  ? handle: script.Handle,
  ? internalId: script.InternalId,
}

script.TypedArrayRemoteValue = {
  type: "typedarray",
  ? handle: script.Handle,
  ? internalId: script.InternalId,
}

script.ArrayBufferRemoteValue = {
  type: "arraybuffer",
  ? handle: script.Handle,
  ? internalId: script.InternalId,
}

script.NodeListRemoteValue = {
  type: "nodelist",
  ? handle: script.Handle,
  ? internalId: script.InternalId,
  ? value: script.ListRemoteValue,
}

script.HTMLCollectionRemoteValue = {
  type: "htmlcollection",
  ? handle: script.Handle,
  ? internalId: script.InternalId,
  ? value: script.ListRemoteValue,
}

script.NodeRemoteValue = {
  type: "node",
  ? sharedId: script.SharedId,
  ? handle: script.Handle,
  ? internalId: script.InternalId,
  ? value: script.NodeProperties,
}

script.NodeProperties = {
  nodeType: js-uint,
  childNodeCount: js-uint,
  ? attributes: {*text => text},
  ? children: [*script.NodeRemoteValue],
  ? localName: text,
  ? mode: "open" / "closed",
  ? namespaceURI: text,
  ? nodeValue: text,
  ? shadowRoot: script.NodeRemoteValue / null,
}

script.WindowProxyRemoteValue = {
  type: "window",
  value: script.WindowProxyProperties,
  ? handle: script.Handle,
  ? internalId: script.InternalId
}

script.WindowProxyProperties = {
  context: browsingContext.BrowsingContext
}
```


#### 2.6.2.15. #### The script.ResultOwnership Type ####

The script.ResultOwnership specifies how the serialized value
ownership will be treated.

```cddl
script.ResultOwnership = "root" / "none"
```


#### 2.6.2.16. #### The script.SerializationOptions Type ####

The script.SerializationOptions allows specifying how ECMAScript
objects will be serialized.

```cddl
script.SerializationOptions = {
  ? maxDomDepth: (js-uint / null) .default 0,
  ? maxObjectDepth: (js-uint / null) .default null,
  ? includeShadowTree: ("none" / "open" / "all") .default "none",
}
```


#### 2.6.2.17. #### The script.SharedId Type ####

The script.SharedId type represents a reference to a DOM Node that
is usable in any realm (including Sandbox Realms).

```cddl
script.SharedId = text;
```


#### 2.6.2.18. #### The script.StackFrame Type ####

A frame in a stack trace is represented by a StackFrame
object. This has a url property, which represents the URL of the
script, a functionName property which represents the name of the
executing function, and lineNumber and columnNumber
properties, which represent the line and column number of the executed code.

```cddl
script.StackFrame = {
  columnNumber: js-uint,
  functionName: text,
  lineNumber: js-uint,
  url: text,
}
```


#### 2.6.2.19. #### The script.StackTrace Type ####

The script.StackTrace type represents the javascript stack at a point in
script execution.

> [!NOTE]
> The details of how to get a list of stack frames, and the properties of
that list are underspecified, and therefore the details here are implementation
defined.

```cddl
script.StackTrace = {
  callFrames: [*script.StackFrame],
}
```


#### 2.6.2.20. #### The script.Source Type ####

The script.Source type represents a script.Realm with
an optional browsingContext.BrowsingContext and related
browser.UserContext in which a script related event occurred.

```cddl
script.Source = {
  realm: script.Realm,
  ? context: browsingContext.BrowsingContext,
  ? userContext: browser.UserContext
}
```


#### 2.6.2.21. #### The script.Target Type ####

script.ContextTarget = {
 context: browsingContext.BrowsingContext,
 ? sandbox: text
}

```cddl
script.RealmTarget = {
  realm: script.Realm
}

script.ContextTarget = {
  context: browsingContext.BrowsingContext,
  ? sandbox: text
}

script.Target = (
  script.ContextTarget /
  script.RealmTarget
)
```


#### 2.6.3.1. #### The script.addPreloadScript Command ####

The script.addPreloadScript command adds a preload
script.

```cddl
script.AddPreloadScript = (
        method: "script.addPreloadScript",
        params: script.AddPreloadScriptParameters
      )

      script.AddPreloadScriptParameters = {
        functionDeclaration: text,
        ? arguments: [*script.ChannelValue],
        ? contexts: [+browsingContext.BrowsingContext],
        ? userContexts: [+browser.UserContext],
        ? sandbox: text
      }
```

```cddl
script.AddPreloadScriptResult = {
        script: script.PreloadScript
      }
```


#### 2.6.3.2. #### The script.disown Command ####

The script.disown command disowns the given handles.
This does not guarantee the handled object will be garbage collected, as there can be
other handles or strong ECMAScript references.

```cddl
script.Disown = (
        method: "script.disown",
        params: script.DisownParameters
      )

      script.DisownParameters = {
        handles: [*script.Handle]
        target: script.Target;
      }
```

```cddl
script.DisownResult = EmptyResult
```


#### 2.6.3.3. #### The script.callFunction Command ####

The script.callFunction command calls a provided
function with given arguments in a given realm.

> [!NOTE]
> In case of an arrow function in functionDeclaration, the
this argument doesn't affect function's this binding.
> [!IMPORTANT]
> TODO: Add timeout argument as described in the script.evaluate.

```cddl
script.CallFunction = (
        method: "script.callFunction",
        params: script.CallFunctionParameters
      )

      script.CallFunctionParameters = {
        functionDeclaration: text,
        awaitPromise: bool,
        target: script.Target,
        ? arguments: [*script.LocalValue],
        ? resultOwnership: script.ResultOwnership,
        ? serializationOptions: script.SerializationOptions,
        ? this: script.LocalValue,
        ? userActivation: bool .default false,
      }
```

```cddl
script.CallFunctionResult = script.EvaluateResult
```


#### 2.6.3.4. #### The script.evaluate Command ####

The script.evaluate command evaluates a provided
script in a given realm. For convenience a navigable can be provided in
place of a realm, in which case the realm used is the realm of the browsing
context's active document.

```cddl
script.Evaluate = (
        method: "script.evaluate",
        params: script.EvaluateParameters
      )

      script.EvaluateParameters = {
        expression: text,
        target: script.Target,
        awaitPromise: bool,
        ? resultOwnership: script.ResultOwnership,
        ? serializationOptions: script.SerializationOptions,
        ? userActivation: bool .default false,
      }
```


#### 2.6.3.5. #### The script.getRealms Command ####

The script.getRealms command returns a list of
all realms, optionally filtered to realms of a specific type, or to the
realm associated with a /navigable's active document.

```cddl
script.GetRealms = (
        method: "script.getRealms",
        params: script.GetRealmsParameters
      )

      script.GetRealmsParameters = {
        ? context: browsingContext.BrowsingContext,
        ? type: script.RealmType,
      }
```

```cddl
script.GetRealmsResult = {
        realms: [*script.RealmInfo]
      }
```


#### 2.6.3.6. #### The script.removePreloadScript Command ####

The script.removePreloadScript command removes a
preload script.

```cddl
script.RemovePreloadScript = (
        method: "script.removePreloadScript",
        params: script.RemovePreloadScriptParameters
      )

      script.RemovePreloadScriptParameters = {
        script: script.PreloadScript
      }
```

```cddl
script.RemovePreloadScriptResult = EmptyResult
```


#### 2.6.4.1. #### The script.message Event ####

script.MessageParameters = {
 channel: script.Channel,
 data: script.RemoteValue,
 source: script.Source,
 }

```cddl
script.Message = (
         method: "script.message",
         params: script.MessageParameters
        )

       script.MessageParameters = {
         channel: script.Channel,
         data: script.RemoteValue,
         source: script.Source,
       }
```


#### 2.6.4.2. #### The script.realmCreated Event ####

When any of the set up a window environment settings object, set up a
worker environment settings object or set up a worklet environment settings
object algorithms are invoked, immediately prior to returning the settings
object:
1. Let |environment settings| be the newly created environment settings
object.
1. Let |realm info| be the result of get the realm info given
|environment settings|.
1. If |realm info| is null, return.
1. Let |related navigables| be the result of get related navigables given |environment settings|.
1. Let |body| be a /map matching the script.RealmCreated
production, with the params field set to |realm info|.
1. For each |session| in the set of sessions for which an event is enabled
given "script.realmCreated" and |related navigables|:
 1. Emit an event with |session| and |body|.

```cddl
script.RealmCreated = (
         method: "script.realmCreated",
         params: script.RealmInfo
        )
```


#### 2.6.4.3. #### The script.realmDestroyed Event ####

script.RealmDestroyedParameters = {
 realm: script.Realm
 }

```cddl
script.RealmDestroyed = (
         method: "script.realmDestroyed",
         params: script.RealmDestroyedParameters
       )

       script.RealmDestroyedParameters = {
         realm: script.Realm
       }
```


## 2.7. ## The storage Module ##

The storage module contains functionality and
events related to storage.


### 2.7.1. ### Definition ###

```cddl
StorageCommand = (
  storage.DeleteCookies //
  storage.GetCookies //
  storage.SetCookie
)
```

```cddl
StorageResult = (
  storage.DeleteCookiesResult /
  storage.GetCookiesResult /
  storage.SetCookieResult
)
```


#### 2.7.2.1. #### The storage.PartitionKey Type ####

The storage.PartitionKey type represents a storage partition key.

```cddl
storage.PartitionKey = {
  ? userContext: text,
  ? sourceOrigin: text,
  Extensible,
}
```


#### 2.7.3.1. #### The storage.getCookies Command ####

The storage.getCookies command retrieves zero or more cookies which match cookie|match a set of provided parameters.

```cddl
storage.GetCookies = (
          method: "storage.getCookies",
          params: storage.GetCookiesParameters
        )

        <!--
        Modifications to this definition should be reflected in
        `network.Cookie`, `network.SetCookieHeader`, and `storage.PartialCookie`.
        -->
        storage.CookieFilter = {
          ? name: text,
          ? value: network.BytesValue,
          ? domain: text,
          ? path: text,
          ? size: js-uint,
          ? httpOnly: bool,
          ? secure: bool,
          ? sameSite: network.SameSite,
          ? expiry: js-uint,
          Extensible,
        }

        storage.BrowsingContextPartitionDescriptor = {
          type: "context",
          context: browsingContext.BrowsingContext
        }

        storage.StorageKeyPartitionDescriptor = {
          type: "storageKey",
          ? userContext: text,
          ? sourceOrigin: text,
          Extensible,
        }

        storage.PartitionDescriptor = (
          storage.BrowsingContextPartitionDescriptor /
          storage.StorageKeyPartitionDescriptor
        )

        storage.GetCookiesParameters = {
          ? filter: storage.CookieFilter,
          ? partition: storage.PartitionDescriptor,
        }
```

```cddl
storage.GetCookiesResult = {
        cookies: [*network.Cookie],
        partitionKey: storage.PartitionKey,
      }
```


#### 2.7.3.2. #### The storage.setCookie Command ####

The storage.setCookie command creates a new cookie in a cookie store, replacing any cookie in that store which matches according to [[COOKIES]].

```cddl
storage.SetCookie = (
          method: "storage.setCookie",
          params: storage.SetCookieParameters,
        )

        <!--
        Modifications to this definition should be reflected in
        `network.Cookie`, `network.SetCookieHeader`, and `storage.CookieFilter`.
        -->
        storage.PartialCookie = {
          name: text,
          value: network.BytesValue,
          domain: text,
          ? path: text,
          ? httpOnly: bool,
          ? secure: bool,
          ? sameSite: network.SameSite,
          ? expiry: js-uint,
          Extensible,
        }

        storage.SetCookieParameters = {
          cookie: storage.PartialCookie,
          ? partition: storage.PartitionDescriptor,
        }
```

```cddl
storage.SetCookieResult = {
        partitionKey: storage.PartitionKey
      }
```


#### 2.7.3.3. #### The storage.deleteCookies Command ####

The storage.deleteCookies command removes zero or more cookies which match cookie|match a set of provided parameters.

```cddl
storage.DeleteCookies = (
          method: "storage.deleteCookies",
          params: storage.DeleteCookiesParameters,
        )

        storage.DeleteCookiesParameters = {
          ? filter: storage.CookieFilter,
          ? partition: storage.PartitionDescriptor,
        }
```

```cddl
storage.DeleteCookiesResult = {
          partitionKey: storage.PartitionKey
        }
```


## 2.8. ## The log Module ##

The log module contains functionality and events
related to logging.


### 2.8.1. ### Definition ###

```cddl
LogEvent = (
  log.EntryAdded
)
```


#### 2.8.3.1. #### The log.entryAdded Event ####

The remote end event trigger is:

```cddl
log.EntryAdded = (
         method: "log.entryAdded",
         params: log.Entry,
        )
```


## 2.9. ## The input Module ##

The input module contains functionality for
simulated user input.


### 2.9.1. ### Definition ###

InputEvent = (
 input.FileDialogOpened
)

```cddl
InputCommand = (
  input.PerformActions //
  input.ReleaseActions //
  input.SetFiles
)
```

```cddl
InputResult = (
  input.PerformActionsResult /
  input.ReleaseActionsResult /
  input.SetFilesResult
)
```

```cddl
InputEvent = (
  input.FileDialogOpened
)
```


#### 2.9.3.1. #### The input.performActions Command ####

The input.performActions command performs a
specified sequence of user input actions.

> [!NOTE]
> for a detailed description of the behavior of this command, see the
actions section of [[WEBDRIVER]].

```cddl
input.PerformActions = (
        method: "input.performActions",
        params: input.PerformActionsParameters
      )

      input.PerformActionsParameters = {
        context: browsingContext.BrowsingContext,
        actions: [*input.SourceActions]
      }

      input.SourceActions = (
        input.NoneSourceActions /
        input.KeySourceActions /
        input.PointerSourceActions /
        input.WheelSourceActions
      )

      input.NoneSourceActions = {
        type: "none",
        id: text,
        actions: [*input.NoneSourceAction]
      }

      input.NoneSourceAction = input.PauseAction

      input.KeySourceActions = {
        type: "key",
        id: text,
        actions: [*input.KeySourceAction]
      }

      input.KeySourceAction = (
        input.PauseAction /
        input.KeyDownAction /
        input.KeyUpAction
      )

      input.PointerSourceActions = {
        type: "pointer",
        id: text,
        ? parameters: input.PointerParameters,
        actions: [*input.PointerSourceAction]
      }

      input.PointerType = "mouse" / "pen" / "touch"

      input.PointerParameters = {
        ? pointerType: input.PointerType .default "mouse"
      }

      input.PointerSourceAction = (
        input.PauseAction /
        input.PointerDownAction /
        input.PointerUpAction /
        input.PointerMoveAction
      )

      input.WheelSourceActions = {
        type: "wheel",
        id: text,
        actions: [*input.WheelSourceAction]
      }

      input.WheelSourceAction = (
        input.PauseAction /
        input.WheelScrollAction
      )

      input.PauseAction = {
        type: "pause",
        ? duration: js-uint
      }

      input.KeyDownAction = {
        type: "keyDown",
        value: text
      }

      input.KeyUpAction = {
        type: "keyUp",
        value: text
      }

      input.PointerUpAction = {
        type: "pointerUp",
        button: js-uint,
      }

      input.PointerDownAction = {
        type: "pointerDown",
        button: js-uint,
        input.PointerCommonProperties
      }

      input.PointerMoveAction = {
        type: "pointerMove",
        x: float,
        y: float,
        ? duration: js-uint,
        ? origin: input.Origin,
        input.PointerCommonProperties
      }

      input.WheelScrollAction = {
        type: "scroll",
        x: js-int,
        y: js-int,
        deltaX: js-int,
        deltaY: js-int,
        ? duration: js-uint,
        ? origin: input.Origin .default "viewport",
      }

      input.PointerCommonProperties = (
        ? width: js-uint,
        ? height: js-uint,
        ? pressure: (0.0..1.0),
        ? tangentialPressure: (-1.0..1.0),
        ? twist: (0..359),
        ; 0 .. Math.PI / 2
        ? altitudeAngle: (0.0..1.5707963267948966),
        ; 0 .. 2 * Math.PI
        ? azimuthAngle: (0.0..6.283185307179586),
      )

      input.Origin = "viewport" / "pointer" / input.ElementOrigin
```

```cddl
input.PerformActionsResult = EmptyResult
```


#### 2.9.3.2. #### The input.releaseActions Command ####

The input.releaseActions command resets the input
state associated with the current session.

```cddl
input.ReleaseActions = (
        method: "input.releaseActions",
        params: input.ReleaseActionsParameters
      )

      input.ReleaseActionsParameters = {
        context: browsingContext.BrowsingContext,
      }
```

```cddl
input.ReleaseActionsResult = EmptyResult
```


#### 2.9.3.3. #### The input.setFiles Command ####

The input.setFiles command sets the files property of a given input element with type file
to a set of file paths.

```cddl
input.SetFiles = (
        method: "input.setFiles",
        params: input.SetFilesParameters
      )

      input.SetFilesParameters = {
        context: browsingContext.BrowsingContext,
        element: script.SharedReference,
        files: [*text]
      }
```

```cddl
input.SetFilesResult = EmptyResult
```


#### 2.9.4.1. #### The input.fileDialogOpened Event ####

input.FileDialogInfo = {
 context: browsingContext.BrowsingContext,
 ? userContext: browser.UserContext,
 ? element: script.SharedReference,
 multiple: bool,
 }

```cddl
input.FileDialogOpened = (
            method: "input.fileDialogOpened",
            params: input.FileDialogInfo
         )

         input.FileDialogInfo = {
            context: browsingContext.BrowsingContext,
            ? userContext: browser.UserContext,
            ? element: script.SharedReference,
            multiple: bool,
         }
```


## 2.10. ## The webExtension Module ##

The webExtension module contains functionality for
managing and interacting with web extensions.


### 2.10.1. ### Definition ###

```cddl
WebExtensionCommand = (
  webExtension.Install //
  webExtension.Uninstall
)
```

```cddl
WebExtensionResult = (
  webExtension.InstallResult /
  webExtension.UninstallResult
)
```


#### 2.10.2.1. #### The webExtension.Extension Type ####

The webExtension.Extension type represents a web extension id within a remote end.

```cddl
webExtension.Extension = text
```


#### 2.10.3.1. #### The webExtension.install Command ####

The webExtension.install command installs a web extension in the remote end.

> [!NOTE]
> Browsers might install the web extension only temporarily by default so
that they will be automatically uninstalled during the next shutdown.

```cddl
webExtension.Install = (
         method: "webExtension.install",
         params: webExtension.InstallParameters
      )

      webExtension.InstallParameters = {
         extensionData: webExtension.ExtensionData,
      }

      webExtension.ExtensionData = (
         webExtension.ExtensionArchivePath /
         webExtension.ExtensionBase64Encoded /
         webExtension.ExtensionPath
      )

      webExtension.ExtensionPath = {
         type: "path",
         path: text,
      }

      webExtension.ExtensionArchivePath = {
         type: "archivePath",
         path: text,
      }

      webExtension.ExtensionBase64Encoded = {
         type: "base64",
         value: text,
      }
```

```cddl
webExtension.InstallResult = {
        extension: webExtension.Extension
      }
```


#### 2.10.3.2. #### The webExtension.uninstall Command ####

The webExtension.uninstall command uninstalls a web extension for the remote end.

```cddl
webExtension.Uninstall = (
         method: "webExtension.uninstall",
         params: webExtension.UninstallParameters
      )

      webExtension.UninstallParameters = {
         extension: webExtension.Extension,
      }
```

```cddl
webExtension.UninstallResult = EmptyResult
```

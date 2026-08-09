# WebDriver BiDi - Extracted Specification & CDDL Schemas

> Sintesi automatizzata per contesto LLM (Descrizioni + Schemi CDDL).



## Definition ##

Title: WebDriver BiDi Shortname: webdriver-bidi Level: None Status: ED Group: browser-testing-tools URL: https://w3c.github.io/webdriver-bidi/ TR: https://www.w3.org/TR/webdriver-bidi/ Repository: w3c/webdriver-bidi Editor: James Graham, Mozilla https://www.mozilla.org, w3cid 40334 Editor: Alex Rudenko, Google https://www.google.com, w3cid 141088 Editor: Maksim Sadym, Google https://www.google.com, w3cid 128970 Abstract: This document defines the BiDirectional WebDriver Protocol, a mechanism for remote control of user agents. Boilerplate: conformance no Complain About: accidental-2119 yes, missing-example-ids yes Default Ref Status: current Indent: 2 Implementation Report: https://wpt.fyi/results/webdriver/tests/bidi Test Suite: https://github.com/web-platform-tests/wpt/tree/master/webdriver/tests/bidi !Channel: #webdriver on irc.w3.org !Wiki: W3C WebDriver Wiki spec: RFC5280; urlPrefix: https://datatracker.ietf.org/doc/html/rfc5280 type: dfn text: Basic Certificate Processing; url: section-6.1.3 spec: RFC6455; urlPrefix: https://datatracker.ietf.org/doc/html/rfc6455 type: dfn text: WebSocket URI; url: section-3 text: Establishes a WebSocket Connection; url: section-4.1 text: Server-Side Requirements; url: section-4.2 text: Reading the Client's Opening Handshake; url: section-4.2.1 text: %x1 denotes a text frame; url: section-5.2 text: Send a WebSocket Message; url: section-6.1 text: A WebSocket Message Has Been Received; url: section-6.2 text: Start The WebSocket Closing Handshake; url: section-7.1.2 text: The WebSocket Closing Handshake is Started; url: section-7.1.3 text: The WebSocket Connection is Closed; url: section-7.1.4 text: Fail the WebSocket Connection; url: section-7.1.7 text: Status Codes; url: section-7.4 text: Handling Errors in UTF-8-Encoded Data; url: section-8.1 spec: RFC8610; urlPrefix: https://datatracker.ietf.org/doc/html/rfc8610 type: dfn text: match a CDDL specification; url: appendix-C spec: RFC6265 type: dfn text: Cookie; url: https://httpwg.org/specs/rfc6265.html text: Cookie store; url: https://httpwg.org/specs/rfc6265.html#storage-model spec: RFC6265bis; urlPrefix: https://datatracker.ietf.org/doc/html/draft-ietf-httpbis-rfc6265bis-20.html type: dfn text: Cookie Lifetime Limits; url: #cookie-lifetime-limits text: Lax; url: section-4.1.2.7 text: Strict; url: section-4.1.2.7 text: Default; url: section-5.6.7.2 spec: WEBDRIVER; urlPrefix: https://w3c.github.io/webdriver/ type: dfn text: WebDriver new session algorithm; url: dfn-webdriver-new-session-algorithms text: accept insecure TLS; url: dfn-accept-insecure-tls text: actions; url: actions text: actions options; url: dfn-actions-options text: active sessions; url: dfn-active-sessions text: additional WebDriver capability; url: dfn-additional-webdriver-capability text: additional capability deserialization algorithm; url: dfn-additional-capability-deserialization-algorithm text: capability name; url: dfn-capability-name text: close the session; url: dfn-close-the-session text: cookie domain; url: dfn-cookie-domain text: cookie expiry time; url: dfn-cookie-expiry-time text: cookie HTTP only; url: dfn-cookie-http-only text: cookie name; url: dfn-cookie-name text: cookie path; url: dfn-cookie-path text: cookie same site; url: dfn-cookie-same-site text: cookie secure only; url: dfn-cookie-secure-only text: cookie value; url: dfn-cookie-value text: create a cookie; url: dfn-creating-a-cookie text: create a session; url: dfn-create-a-session text: dispatch actions; url: dfn-dispatch-actions text: dispatch tick actions; url: dfn-dispatch-tick-actions text: draw a bounding box from the framebuffer; url: dfn-draw-a-bounding-box-from-the-framebuffer text: endpoint node; url: dfn-endpoint-node text: error code; url: dfn-error-code text: error; url: errors text: extract an action sequence; url: dfn-extract-an-action-sequence text: get a node; url: dfn-get-a-node text: get element origin; url: dfn-get-element-origin text: get or create a node reference; url: dfn-get-or-create-a-node-reference text: get the input state; url: dfn-get-the-input-state text: getting a property; url: dfn-getting-properties text: http session; url: dfn-http-session text: input cancel list; url: dfn-input-cancel-list text: intermediary node; url: dfn-intermediary-nodes text: invalid argument; url: dfn-invalid-argument text: invalid selector; url: dfn-invalid-selector text: invalid session id; url: dfn-invalid-session-id text: is element origin; url: dfn-is-element-origin text: local end; url: dfn-local-ends text: matched capability serialization algorithm; url: dfn-matched-capability-serialization-algorithm text: maximum active sessions; url: dfn-maximum-active-sessions text: no such alert; url: dfn-no-such-alert text: no such element; url: dfn-no-such-element text: no such frame; url: dfn-no-such-frame text: parse a page range; url: dfn-parse-a-page-range text: handler; for: prompt handler configuration; url: dfn-handler text: process capabilities; url: dfn-capabilities-processing text: proxy configuration; url: dfn-proxy-configuration text: readiness state; url: dfn-readiness-state text: remote end steps; url: dfn-remote-end-steps text: remote end; url: dfn-remote-ends text: reset the input state; url: dfn-reset-the-input-state text: scroll into view; url: dfn-scrolls-into-view text: session ID; url: dfn-session-id text: session not created; url: dfn-session-not-created text: session; url: dfn-webdriver-session text: set a property; url: dfn-set-a-property text: success; url: dfn-success text: table for cookie conversion; url: dfn-table-for-cookie-conversion text: try; url: dfn-try text: trying; url: dfn-try text: unable to capture screen; url: dfn-unable-to-capture-screen text: unknown command; url: dfn-unknown-command text: unknown error; url: dfn-unknown-error text: user prompt handler; url: dfn-user-prompt-handler text: unsupported operation; url: dfn-unsupported-operation text: web element reference; url: dfn-web-element-reference text: webdriver-active flag; url: dfn-webdriver-active-flag text: window handle; url: dfn-window-handles spec: CONSOLE; urlPrefix: https://console.spec.whatwg.org type: dfn text: formatter; url: formatter text: formatting specifier; url: formatting-specifiers text: printer; url: printer spec: ECMASCRIPT-I18N; urlPrefix: https://tc39.es/ecma402/ type: dfn text: DefaultLocale; url: #sec-defaultlocale text: IsStructurallyValidLanguageTag; url: #sec-isstructurallyvalidlanguagetag spec: ECMASCRIPT; urlPrefix: https://tc39.es/ecma262/ type: dfn text: Array; url: sec-array-objects text: AvailableNamedTimeZoneIdentifiers; url: sec-availablenamedtimezoneidentifiers text: Await; url: await text: BigInt; url: sec-bigint-constructor text: Call; url: sec-call text: Completion Record; url: sec-completion-record-specification-type text: Construct; url: sec-construct text: CreateArrayFromList; url: sec-createarrayfromlist text: CreateArrayIterator; url: sec-createarrayiterator text: CreateBuiltinFunction; url: sec-createbuiltinfunction text: CreateListFromArrayLike; url: sec-createlistfromarraylike text: CreateMapIterator; url: sec-createmapiterator text: CreateSetIterator; url: sec-createsetiterator text: Date Time String Format; url: sec-date-time-string-format text: Date.prototype.toISOString; url: sec-date.prototype.toisostring text: Date; url: sec-date-constructor text: EnumerableOwnPropertyNames; url: sec-enumerableownpropertynames text: Get; url: sec-get-o-p text: GetIterator; url: sec-getiterator text: HasProperty; url: sec-hasproperty text: IsArray; url: sec-isarray text: IsCallable; url: sec-iscallable text: IsPromise; url: sec-ispromise text: IsRegExp; url: sec-isregexp text: IsTimeZoneOffsetString; url: sec-istimezoneoffsetstring text: IteratorToList; url: sec-iteratortolist text: LengthOfArrayLike; url: sec-lengthofarraylike text: Map; url: #sec-map-iterable; for: constructor text: Number; url: sec-number-constructor text: Object.fromEntries; url: sec-object.fromentries text: Object; url: sec-object-objects text: RegExp; url: sec-regexp-pattern-flags text: ScriptEvaluation; url: sec-runtime-semantics-scriptevaluation text: Set object; url: sec-set-objects text: String; url: sec-string-constructor text: StringToBigInt; url: sec-stringtobigint text: StringToNumber; url: sec-stringtonumber text: SystemTimeZoneIdentifier; url: sec-systemtimezoneidentifier text: ToString; url: sec-tostring text: Type; url: sec-ecmascript-data-types-and-values text: abrupt completion; url: sec-completion-record-specification-type text: boolean; url: sec-terms-and-definitions-boolean-value text: current realm record; url: current-realm text: internal slot; url: sec-object-internal-methods-and-internal-slots text: null; url: sec-null-value text: primitive ECMAScript value; url: sec-primitive-value text: realm; url: sec-code-realms text: running execution context; url: running-execution-context text: throw completion; url: sec-completion-record-specification-type text: test; url: #sec-regexp.prototype.test text: time value; url: sec-time-values-and-time-range text: undefined; url: sec-undefined-value spec: FETCH; urlPrefix: https://fetch.spec.whatwg.org/ type: dfn text: response; url: #concept-response spec: GEOMETRY; urlPrefix: https://drafts.fxtf.org/geometry/ type: dfn text: rectangle; url: rectangle text: x coordinate; url: rectangle-x-coordinate text: y coordinate; url: rectangle-y-coordinate text: width dimension; url: rectangle-width-dimension text: height dimension; url: rectangle-height-dimension spec: GEOLOCATION; urlPrefix: https://www.w3.org/TR/geolocation/ type: dfn text: GeolocationPositionError; url: #dom-geolocationpositionerror text: POSITION_UNAVAILABLE; url: #dom-geolocationpositionerror-position_unavailable text: set emulated position data; url: #dfn-set-emulated-position-data spec: SCREEN-ORIENTATION; urlPrefix: https://www.w3.org/TR/screen-orientation type: dfn text: current orientation angle; url: #dfn-current-orientation-angle text: current orientation type; url: #dfn-current-orientation-type text: screen orientation; url: #dom-screenorientation text: screen orientation change steps; url: #dfn-screen-orientation-change-steps text: screen orientation values lists; url: #dfn-screen-orientation-values-lists spec: HTML; urlPrefix: https://html.spec.whatwg.org/multipage/ type: dfn text: 2D context creation algorithm; url: canvas.html#2d-context-creation-algorithm text: 2D; url: canvas.html#concept-canvas-2d text: a serialization of the bitmap as a file; url: canvas.html#a-serialisation-of-the-bitmap-as-a-file text: activation notification; url: interaction.html#activation-notification text: active window; url: document-sequences.html#nav-window text: alert; url: timers-and-user-prompts.html#dom-alert text: associated `Document`; url: nav-history-apis.html#concept-document-window text: close; url: document-sequences.html#close-a-top-level-traversable text: disabled; url: form-control-infrastructure.html#concept-fe-disabled text: File Upload state; url: input.html#file-upload-state-(type=file) text: confirm; url: timers-and-user-prompts.html#dom-confirm text: context mode; url: /canvas.html#offscreencanvas-context-mode text: create a classic script; url: webappapis.html#creating-a-classic-script text: create a new browsing context; url: browsers.html#creating-a-new-browsing-context text: create a new top-level traversable; url: document-sequences.html#creating-a-new-top-level-traversable text: default script fetch options; url: webappapis.html#default-script-fetch-options text: default view; url: nav-history-apis.html#dom-document-defaultview text: descendant navigables; url: document-sequences.html#descendant-navigables text: environment settings object's Realm; url: webappapis.html#environment-settings-object's-realm text: focused area of the document; url: interaction.html#focused-area-of-the-document text: getting all used history steps; url:browsing-the-web.html#getting-all-used-history-steps text: hidden; url: document-sequences.html#system-visibility-state text: history handling behavior; url: browsing-the-web.html#history-handling-behavior text: innerText getter steps; url:dom.html#dom-innertext text: input type; url: input.html#dom-input-type text: navigable; for:window; url: nav-history-apis.html#window-navigable text: navigables; url: document-sequences.html#navigables text: navigation id; url: browsing-the-web.html#navigation-id text: ongoing-navigation; url: browsing-the-web.html#ongoing-navigation text: origin-clean; url: canvas.html#concept-canvas-origin-clean text: parent; for:navigable; url: document-sequences.html#nav-parent text: prompt to unload; url: browsing-the-web.html#prompt-to-unload-a-document text: prompt; url: timers-and-user-prompts.html#dom-prompt text: report an error; url: webappapis.html#report-the-error text: run the animation frame callbacks; url: imagebitmap-and-animations.html#run-the-animation-frame-callbacks text: same origin domain; url: browsers.html#same-origin-domain text: select an image source from a source set; url: images.html#select-an-image-source-from-a-source-set text: selected files; url: input.html#concept-input-type-file-selected text: session history entry; url: browsing-the-web.html#session-history-entry text: session history traversal queue; url: document-sequences.html#tn-session-history-traversal-queue text: session history; url: history.html#session-history text: set up a window environment settings object; url: nav-history-apis.html#set-up-a-window-environment-settings-object text: set up a worker environment settings object; url: workers.html#set-up-a-worker-environment-settings-object text: set up a worklet environment settings object; url: worklets.html#set-up-a-worklet-environment-settings-object text: shared worker; url: workers.html#shared-workers text: system visibility state; url: document-sequences.html#system-visibility-state text: traversable navigable; url:document-sequences.html#traversable-navigable text: traverse the history by a delta; url: browsing-the-web.html#traverse-the-history-by-a-delta text: update the file selection; url: input.html#update-the-file-selection text: visible; url: document-sequences.html#system-visibility-state text: worker event loop; url: webappapis.html#worker-event-loop-2 text: worklet global scopes; url:worklets.html#concept-document-worklet-global-scopes spec: INFRA; urlPrefix: https://infra.spec.whatwg.org/ type: dfn text: break; url: iteration-break text: convert a JSON-derived JavaScript value to an Infra value; url: convert-a-json-derived-javascript-value-to-an-infra-value spec: RESOURCE-TIMING; urlPrefix: https://w3c.github.io/resource-timing/ type: dfn text: convert fetch timestamp; url: dfn-convert-fetch-timestamp spec: HR-TIME; urlPrefix: https://w3c.github.io/hr-time/ type: dfn text: get time origin timestamp; url: get-time-origin-timestamp spec: RFC4648; urlPrefix: https://datatracker.ietf.org/doc/html/rfc4648 type: dfn text: Base64 Encode; url: section-4 spec: CSS-OVERFLOW-3; urlPrefix: https://drafts.csswg.org/css-overflow-3/ type: dfn text: classic scrollbars; url: #classic-scrollbars text: overlay scrollbars; url: #overlay-scrollbars spec: CSS-VALUES-3; urlPrefix: https://drafts.csswg.org/css-values-3/ type: dfn text: absolute lengths; url: #absolute-lengths spec: CSSOM-VIEW; urlPrefix: https://drafts.csswg.org/cssom-view/ type: dfn text: CSS pixel; url: #dom-window-devicepixelratio text: evaluate media queries and report changes; url: #evaluate-media-queries-and-report-changes text: layout viewport; url: #layout-viewport text: scroll height; url: #dom-element-scrollheight text: scroll width; url: #dom-element-scrollwidth text: visual viewport page left; url: #dom-visualviewport-pageleft text: visual viewport page top; url: #dom-visualviewport-pagetop text: visual viewport; url: #visual-viewport text: web-exposed available screen area; url: #web-exposed-available-screen-area text: web-exposed screen area; url: #web-exposed-screen-area spec: DOM; urlPrefix: https://dom.spec.whatwg.org/ type: dfn text: root; url: #concept-tree-root text: document element; url: #ref-for-dom-document-documentelement text: evaluate; url: #dom-xpathevaluatorbase-evaluate text: nodes; url: #concept-node text: ORDERED_NODE_SNAPSHOT_TYPE; url: #dom-xpathresult-ordered_node_snapshot_type text: snapshotItem; url: #dom-xpathresult-snapshotitem spec: FULLSCREEN; urlPrefix: https://fullscreen.spec.whatwg.org/ type: dfn text: fullscreen an element; url: #fullscreen-an-element text: fullscreen is supported; url: #fullscreen-is-supported text: fully exit fullscreen; url: #fully-exit-fullscreen spec: SELECTORS4; urlPrefix: https://drafts.csswg.org/selectors-4/ type: dfn text: match a selector against a tree; url: #match-a-selector-against-a-tree text: parse a selector; url: #parse-a-selector text: scoping root; url: #scoping-root spec: WEB-IDL; urlPrefix: https://webidl.spec.whatwg.org/ type: dfn text: DOMException; url: #idl-DOMException text: SyntaxError; url: #syntaxerror spec: UNICODE; urlPrefix: https://www.unicode.org/versions/Unicode15.0.0/ type: dfn text: Unicode Default Case Conversion algorithm; url: ch03.pdf#G34944 text: toUppercase; url: ch03.pdf#G34078 spec: ACCNAME; urlPrefix:https://www.w3.org/TR/accname-1.2 type: dfn text: accessible name; url: /#dfn-accessible-name spec: CORE-AAM; urlPrefix:https://www.w3.org/TR/core-aam-1.2 type: dfn text: computed role; url: /#roleMappingComputedRole spec: MEDIAQUERIES4; urlPrefix: https://drafts.csswg.org/mediaqueries-4/ type: dfn text: resolution media feature; url: #resolution text: media type; url: #media-type text: media feature; url: #media-features text: mf-name; url: #typedef-mf-name spec: RFC9110; urlPrefix: https://httpwg.org/specs/rfc9110.html type: dfn text: field-name token; url: #fields.names text: method token; url: #method.overview spec: SCREEN-CAPTURE; urlPrefix: https://www.w3.org/TR/screen-capture/ type: dfn text: browser; url: #dfn-browser text: display surface; url: dfn-display-surface spec: TOUCH-EVENTS; urlPrefix: https://www.w3.org/community/reports/touchevents/CG-FINAL-touch-events-20240704/ type: dfn text: expose legacy touch event APIs; url: #conditionally-exposing-legacy-touch-event-apis spec: WebSockets; urlPrefix: https://websockets.spec.whatwg.org/ type: dfn text: WebSocket; url: #websocket spec: WebTransport; urlPrefix: https://w3c.github.io/webtransport/ type: dfn text: Cleanup WebTransport; url: #webtransport-cleanup var { color: #cd5c5c } /** * Emulate the appearace of the so-called "simple" table provided by ReSpec, as * used in WebDriver Classic. */ table.respec-simple { border-spacing: 0; border-collapse: collapse; border-bottom: 3px solid #005a9c; } table.respec-simple th { background: #005a9c; color: #fff; padding: 3px 5px; text-align: left; } table.respec-simple tr:nth-child(2n) { background: #f0f6ff; } table.respec-simple td { padding: 3px 10px; border-top: 1px solid #ddd; } [[WEBDRIVER|WebDriver]] defines a protocol for introspection and remote control of user agents. This specification extends WebDriver by introducing bidirectional communication. In place of the strict command/response format of WebDriver, this permits events to stream from the user agent to the controlling software, better matching the evented nature of the browser DOM. This specification depends on the Infra Standard. [[!INFRA]] Network protocol messages are defined using CDDL. [[!RFC8610]] This specification defines a <dfn>wait queue</dfn> which is a /map. Issue: Surely there's a better mechanism for doing this "wait for an event" thing. A <dfn>WebDriver configuration</dfn> is a struct with: * struct/item <dfn for="WebDriver configuration">global</dfn> which is a WebDriver configuration/value, initially WebDriver configuration/unset; * struct/item <dfn for="WebDriver configuration">user contexts</dfn> which is a weak map between user context|user contexts and WebDriver configuration/value, initially empty; * struct/item <dfn for="WebDriver configuration">navigables</dfn> which is a weak map between /navigables and WebDriver configuration/value, initially empty. A WebDriver configuration has an <dfn for="WebDriver configuration">associated type</dfn> which is a type. The <dfn for="WebDriver configuration">value</dfn> for a WebDriver configuration is either a value whose type is the WebDriver configuration/associated type for that configuration or WebDriver configuration/unset. WebDriver configuration/value has not been set. This section defines the basic concepts of the WebDriver BiDi protocol. These terms are distinct from their representation at the The protocol is defined using a [[!RFC8610|CDDL]] definition. For the convenience of implementers two separate CDDL definitions are defined; the on the local end and consumed on the remote end, and the <dfn cddl-module export lt="Local end definition|local end definition|local-cddl">local end definition</dfn> which defines the format of messages produced on the remote end and consumed on the local end Issue: Should this be an appendix? This section gives the initial contents of the {^remote end definition^} and {^local end definition^}. These are augmented by the definition fragments defined in the remainder of the specification. {^Remote end definition^}

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

{^Local end definition^}

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

An <dfn export>EmptyResult</dfn> is a result type with no required fields, used as the return type for commands that don't produce result data. {^Remote end definition^} and {^Local end definition^}

```cddl
Extensible = (*text => any)

js-int = -9007199254740991..9007199254740991
js-uint = 0..9007199254740991
```


## Session ##


## Modules ##


## Commands ##


## Errors ##

WebDriver BiDi extends the /session concept from [[WEBDRIVER|WebDriver]]. A /session has a <dfn>BiDi flag</dfn>, which is false unless otherwise stated. A <dfn export>BiDi session</dfn> is a /session which has the BiDi flag set to true. The WebDriver BiDi protocol is organized into modules. Each <dfn export>module</dfn> represents a collection of related commands and events pertaining to a certain aspect of the user agent. For example, a module might contain functionality for inspecting and manipulating the DOM, or for script execution. Each module has a <dfn for=module export>module name</dfn> which is a string. The command name and event name for commands and events defined in the module start with the module name followed by a period "<code>.</code>". Modules which contain commands define {^remote end definition^} fragments. These provide choices in the <code>CommandData</code> group for the module's commands, and can also define additional definition properties. They can also define {^local end definition^} fragments that provide additional choices in the <code>ResultData</code> group for the results of commands in the module. Modules which contain events define {^local end definition^} fragments that are choices in the <code>Event</code> group for the module's events. An implementation may define <dfn export>extension modules</dfn>. These must have a module name that contains a single colon "<code>:</code>" character. The part before the colon is the prefix; this is typically the same for all extension modules specific to a given implementation and should be unique for a given implementation. Other specifications may define their own WebDriver-BiDi modules that extend the protocol. Such modules must not have a name which contains a colon (<code>:</code>) character, nor must they define command names, event names, or property names that contain that character. Authors of external specifications are encouraged to to add new modules rather than extending existing ones. Where it is desired to extend an existing module, it is preferred to integrate the extension directly into the specification containing the original module definition. A <dfn export>command</dfn> is an asynchronous operation, requested by the local end and run on the remote end, resulting in either a result or an error being returned to the local end. Multiple commands can run at the same time, and commands can potentially be long-running. As a consequence, commands can finish out-of-order. Each command is defined by: - A <dfn export for=command>command type</dfn> which is defined by a {^remote end definition^} fragment containing a group. Each such group has two fields: - <code>method</code> which is a string literal of the form <code>[module name].[method name]</code>. This is the <dfn export for=command>command name</dfn>. - <code>params</code> which defines a mapping containing data that to be passed into the command. The populated value of this map is the - A <dfn export for=command>result type</dfn>, which is defined by a {^local end definition^} fragment. - A set of remote end steps which define the actions to take for a command given a BiDi session and command parameters and return an instance of the command result type. A command that can run without an active session is a <dfn export>static command</dfn>. Commands are not static commands unless stated in their definition. When commands are sent from the local end they have a command id. This is an identifier used by the local end to identify the response from a particular command. From the point of view of the remote end this identifier is opaque and cannot be used internally to identify the command. and isn't necessarily unique over the course of a session. For example a local end which ignores all responses could use the same command id for each command. The <dfn export>set of all command names</dfn> is a /set containing all the defined command names, including any belonging to extension modules. WebDriver BiDi extends the set of error codes from [[WEBDRIVER|WebDriver]] with the following additional codes:

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


## Events ##


## Establishing a Connection ##


## Sandbox Realms ##


## Sandbox Proxy Objects ##


## SandboxWindowProxy ##


## The session Module ##


### Definition ###

An <dfn export>event</dfn> is a notification, sent by the remote end to the local end, signaling that something of interest has occurred on the remote end. - An <dfn export for=event>event type</dfn> is defined by a {^local end definition^} fragment containing a group. Each such group has two fields: - <code>method</code> which is a string literal of the form <code>[module name].[event name]</code>. This is the <dfn export for=event>event name</dfn>. - <code>params</code> which defines a mapping containing event data. The populated value of this map is the <dfn export for=event>event parameters</dfn>. - A <dfn for=event export>remote end event trigger</dfn> which defines when the event is triggered and steps to construct the event type data. - Optionally, a set of <dfn for=event export>remote end subscribe steps</dfn>, which define steps to take when a local end subscribes to an event. Where defined these steps have an associated <dfn for=event export>subscribe priority</dfn> which is an integer controlling the order in which the steps are run when multiple events are enabled at once, with lower integers indicating steps that run earlier. A BiDi session has <dfn for=event>subscriptions</dfn> which is a /list of subscriptions. A BiDi session has a <dfn for=event>known subscription ids</dfn> which is a /set of all subscription/subscription ids that have been issued to the local end but which have not yet been unsubscribed. A <dfn for=event>subscription</dfn> is a /struct consisting of a and <dfn for=subscription>user context ids</dfn> (a /set of IDs of user context|user contexts). A subscription |subscription| is <dfn for="subscription">global</dfn> if |subscription|'s subscription/top-level traversable ids is an empty set and |subscription|'s user context ids is an empty set. Message transport is provided using the WebSocket protocol. [[!RFC6455]] client and the remote end is the server / remote host. similar to JSON-RPC, but this specification does not normatively reference it. [[JSON-RPC]] The normative requirements on remote ends are instead given as a precise processing model, while no normative requirements are given for local ends. A <dfn>WebSocket listener</dfn> is a network endpoint that is able to accept incoming [[!RFC6455|WebSocket]] connections. A WebSocket listener has a <dfn for=listener>host</dfn>, a <dfn for=listener>port</dfn>, a <dfn for=listener>secure flag</dfn>, and a When a WebSocket listener |listener| is created, a remote end must start to listen for WebSocket connections on the host and port given by |listener|'s listener/host and listener/port. If |listener|'s listener/secure flag is set, then connections established from |listener| must be TLS encrypted. A remote end has a /set of WebSocket listeners <dfn>active listeners</dfn>, which is initially empty. A remote end has a /set of <dfn>WebSocket connections not associated with a session</dfn>, which is initially empty. A <dfn>WebSocket connection</dfn> is a network connection that follows the requirements of the [[!RFC6455|WebSocket protocol]] A BiDi session has a /set of <dfn>session WebSocket connections</dfn> whose elements are WebSocket connections. This is initially empty. A BiDi session |session| is <dfn>associated with connection</dfn> |connection| if |session|'s session WebSocket connections contains |connection|. session=]. When a client establishes a WebSocket connection |connection| by connecting to one of the set of active listeners |listener|, the implementation must proceed according to the WebSocket server-side requirements, with the following steps run when deciding whether to accept the incoming connection: 1. Let |resource name| be the resource name from reading the client's opening handshake. If |resource name| is not in |listener|'s list of WebSocket resources, then stop running these steps and act as if the requested service is not available. 1. If |resource name| is the byte string "<code>/session</code>", and the implementation supports BiDi-only sessions: 1. Run any other implementation-defined steps to decide if the connection should be accepted, and if it is not stop running these steps and act as if the requested service is not available. 1. Add the connection to WebSocket connections not associated with a session. 1. Return. 1. Get a session ID for a WebSocket resource with |resource name| and let |session id| be that value. If |session id| is null then stop running these steps and act as if the requested service is not available. 1. If there is a /session in the list of active sessions with |session id| as its session ID then let |session| be that session. Otherwise stop running these steps and act as if the requested service is not available. 1. Run any other implementation-defined steps to decide if the connection should be accepted, and if it is not stop running these steps and act as if the requested service is not available. 1. Otherwise append |connection| to |session|'s session WebSocket connections, and proceed with the WebSocket server-side requirements when a server chooses to accept an incoming connection. Issue: Do we support > 1 connection for a single session? When a WebSocket message has been received for a WebSocket connection |connection| with type |type| and data |data|, a remote end must handle an incoming message given |connection|, |type| and |data|. When the WebSocket closing handshake is started or when the WebSocket connection is closed for a WebSocket connection |connection|, a remote end must handle a connection closing given |connection|. WebSocket connection to be closed without a closing handshake. or many WebSocket listeners. [[!WEBDRIVER|WebDriver]] defines that an endpoint node supports at most one session at a time, so it's expected to only have a single listener. typically be "<code>localhost</code>". WebDriver clients opt in to a bidirectional connection by requesting the WebSocket URL capability with value true. A common requirement for automation tools is to execute scripts which have access to the DOM of a document, but don't have information about any changes to the DOM APIs made by scripts running in the navigable containing the document. A BiDi session has a <dfn>sandbox map</dfn> which is a weak map in which the keys are Window objects, and the values are maps between strings and SandboxWindowProxy objects. existing implementations. It exposes parts of the implementations that have previously been considered internal by specifications, in particular the distinction between the internal state of platform objects (which is typically implemented as native objects in the main implementation language of the browser engine) and the ECMAScript-visible state. Because existing sandbox implementations happen at a low level in the engine, implementations converging toward the specification in all details might be a slow process. In the meantime, implementers are encouraged to provide detailed documentation on any differences with the specification, and users of this feature are encouraged to explicitly test that scripts running in sandboxes work in all implementations. Each sandbox is a unique ECMAScript Realm. However the sandbox realm provides access to platform objects in an existing Window realm via SandboxProxy objects. A <dfn interface>SandboxProxy</dfn> object is an exotic object that mediates sandboxed access to objects from another realm. Sandbox proxy objects are designed to enforce the following restrictions: * Platform objects are accessible, but property access returns only Web IDL-defined properties and not ECMAScript-defined properties (either "expando" properties that are not present in the underlying interface, or ECMAScript-defined properties that shadow a property in the underlying interface). * Setting a property either runs Web IDL-defined setter steps, or sets a property on the proxy object. This means that properties written outside the sandbox are not accessible, but interface members can be used as normal. There is no SandboxProxy interface object. Issue: Define in detail how SandboxProxy works A <dfn interface>SandboxWindowProxy</dfn> is an exotic object that represents a Window object wrapped by a SandboxProxy object. This provides sandboxed access to that data in a Window global. Issue: Define how this works. A <dfn export>user context</dfn> represents a collection of zero or more /top-level traversables within a remote end. Each user context has an associated storage partition, so that remote end data is not shared between different user context|user contexts. Issue: Unclear that this is the best way to formally define the concept of a user context or the interaction with storage. user context|user contexts. However, this is not compatible with usage of the term "user agent" to mean the entire web client with multiple user context|user contexts. Although this difference is not visible to web content, it is observed via WebDriver, so we avoid using this terminology. A user context has a <dfn export for="user context">user context id</dfn>, which is a unique string set upon the user context creation. A /navigable has an <dfn export>associated user context</dfn>, which is a user context. When a new /top-level traversable is created its associated user context is set to a user context in the set of user contexts. /top-level traversable is created, however in cases where no such requirements are present, the associated user context for a /top-level traversable is implemenation-defined. Issue: Should we specify that /top-level traversables with a non-null opener have the same associated user context as their opener? Need to check if this is something existing implementations enforce. A child navigable's associated user context is it's navigable/parent's associated user context. A user context which isn't the associated user context for any /top-level traversable is an <dfn>empty user context</dfn>. The <dfn>default user context</dfn> is a user context with user context id <code>"default"</code>. An implementation has a <dfn>set of user contexts</dfn>, which is a /set of user context|user contexts. Initially this contains the default user context. Implementations may set/append new user context|user contexts to the set of user contexts at any time, for example in response to user actions. implementation might always have multiple entries in the set of user contexts. Implementations may set/remove any empty user context, with exception of the default user context, from the set of user contexts at any time. However they are not required to remove such user context|user contexts. user context|User contexts that are not empty user contexts must not be removed from the set of user contexts. A BiDi session has a /map between user context|user contexts and boolean. A BiDi session has a <dfn>user context to proxy configuration map</dfn>, which is a /map between user context|user contexts and proxy configuration. An <dfn>emulated network conditions struct</dfn> is a struct with: * struct/item named <dfn id="emulated-network-conditions-struct-offline" for="emulated-network-conditions-struct">offline</dfn> which is a boolean or null. A BiDi session has a <dfn for=session>emulated network conditions</dfn> which is a struct with an struct/item named <dfn for="emulated network conditions">default network conditions</dfn>, which is an emulated network conditions struct or null, an struct/item named is a weak map between user context|user contexts and emulated network conditions struct, and a struct/item named weak map between /navigables and emulated network conditions struct. When a user context is set/remove|removed from the set of user contexts, remove user context subscriptions. The <dfn export for=modules>session</dfn> module contains commands and events for monitoring the status of the remote end. {^remote end definition^}

```cddl
SessionCommand = (
  session.End //
  session.New //
  session.Status //
  session.Subscribe //
  session.Unsubscribe
)
```

{^local end definition^}

```cddl
SessionResult = (
  session.EndResult /
  session.NewResult /
  session.StatusResult /
  session.SubscribeResult /
  session.UnsubscribeResult
)
```


### Types ###


#### The session.CapabilitiesRequest Type ####

```cddl
session.CapabilitiesRequest = {
  ? alwaysMatch: session.CapabilityRequest,
  ? firstMatch: [*session.CapabilityRequest]
}
```


#### The session.CapabilityRequest Type ####

The <code>session.CapabilitiesRequest</code> type represents the capabilities requested for a session. {^remote end definition^} and {^local end definition^}

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


#### The session.ProxyConfiguration Type ####

The <code>session.CapabilityRequest</code> type represents a specific set of requested capabilities. WebDriver BiDi defines additional WebDriver capability|additional WebDriver capabilities. The following tables enumerates the capabilities each implementation must support for WebDriver BiDi. Capability: <dfn>WebSocket URL</dfn> Key: "<code>webSocketUrl</code>" Value type: boolean Description: Defines the current session's support for bidirectional connection. {^remote end definition^} and {^local end definition^}

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


#### The session.UserPromptHandler Type ####

{^Remote end definition^} and {^local end definition^}

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


#### The session.UserPromptHandlerType Type ####

The <code>session.UserPromptHandler</code> type represents the configuration of the user prompt handler. the picker. "ignore" keeps the picker open. {^Remote end definition^} and {^local end definition^}

```cddl
session.UserPromptHandlerType = "accept" / "dismiss" / "ignore";
```


#### The session.Subscription Type ####

The <code>session.UserPromptHandlerType</code> type represents the behavior of the user prompt handler.

```cddl
session.Subscription = text
```


#### The session.SubscribeParameters Type ####

The <code>session.Subscription</code> type represents a unique subscription identifier.

```cddl
session.SubscribeParameters = {
  events: [+text],
  ? contexts: [+browsingContext.BrowsingContext],
  ? userContexts: [+browser.UserContext],
}
```


#### The session.UnsubscribeByIDRequest Type ####

The <code>session.SubscribeParameters</code> type represents a request to subscribe to a specific set of events.

```cddl
session.UnsubscribeByIDRequest = {
  subscriptions: [+session.Subscription],
}
```


#### The session.UnsubscribeByAttributesRequest Type ####

The <code>session.UnsubscribeByIDRequest</code> type represents a request to remove event subscriptions identified by subscription IDs.

```cddl
session.UnsubscribeByAttributesRequest = {
  events: [+text],
}
```


### Commands ###


#### The session.status Command ####

The <code>session.UnsubscribeByAttributesRequest</code> type represents a request to unsubscribe using subscription attributes. The <dfn export for=commands>session.status</dfn> command returns information about whether a remote end is in a state in which it can create new sessions, but may additionally include arbitrary meta information that is specific to the implementation. This is a static command.

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


#### The session.new Command ####

The <dfn export for=commands>session.new</dfn> command allows creating a new BiDi session. This is a static command.

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


#### The session.end Command ####

The <dfn export for=commands>session.end</dfn> command ends the current /session.

```cddl
session.End = (
        method: "session.end",
        params: EmptyParams
      )
```

```cddl
session.EndResult = EmptyResult
```


#### The session.subscribe Command ####

The <dfn export for=commands>session.subscribe</dfn> command enables certain events either globally or for a set of navigables. Issue: This needs to be generalized to work with realms too.

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


#### The session.unsubscribe Command ####

The <dfn export for=commands>session.unsubscribe</dfn> command disables events either globally or for a set of navigables. Issue: This needs to be generalised to work with realms too.

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


## The browser Module ##


### Definition ###

The <dfn export for=modules>browser</dfn> module contains commands for managing the remote end browser process. {^remote end definition^}

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

{^local end definition^}

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


### Windows ###


### Types ###


#### The browser.ClientWindow Type ####

Each /top-level traversable is associated with a single <dfn>client window</dfn> which represents a rectangular area containing the traversable=]'s active document when its visibility state is "<code>visible</code>", as well as any browser-specific user interface elements associated with displaying the traversable (e.g. any URL bar, toolbars, or OS window decorations). A client window has a <dfn>client window id</dfn> which is a string uniquely identifying that window. A client window has an <dfn for="client window">x-coordinate</dfn>, which is the number of CSS pixels between the left edge of the web-exposed screen area and the left edge of the window, or zero if that doesn't make sense for a particular window. A client window has a <dfn for="client window">y-coordinate</dfn>, which is the number of CSS pixels between the top edge of the web-exposed screen area and the top edge of the window, or zero if that doesn't make sense for a particular window. A client window has a <dfn for="client window">width</dfn>, which is the width of the window's rectangle in CSS pixels. A client window has a <dfn for="client window">height</dfn>, which is the height of the window's rectangle in CSS pixels. To <dfn>maximize the client window</dfn> |window| an implementation should either perform steps corresponding to the platform notion of maximizing |window|, or position |window| such that its client window/x-coordinate is as close as possible to 0, its client window/y-coordinate is as close as possible to 0, its client window/width is as close as possible to the width of the web-exposed screen area and its client window/height is as close as possible to the height of the web-exposed screen area. If either of these options are supported then <dfn>maximize client window is supported</dfn>. To <dfn>minimize the client window</dfn> |window| an implementation should either perform steps corresponding to the platform notion of minimizing |window|, or otherwise hide |window| such that all the active documents in /top-level traversables associated with |window| have visibility state "<code>hidden</code>" and |window|'s client window/width and client window/height are both as close as possible to 0. If either of these options are supported then <dfn>minimize client window is supported</dfn>. To <dfn>restore the client window</dfn> |window| an implementation should ensure that it's neither in a platform-defined maximized state, nor in a platform-defined minimized state, and that if there is one or more /top-level traversable associated with |window|, at least one of those has an active document in the "<code>visible</code>" state. If this is supported then <dfn>restore client window is supported</dfn>.

```cddl
browser.ClientWindow = text;
```


#### The browser.ClientWindowInfo Type ####

The <code>browser.ClientWindow</code> uniquely identifies a client window.

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


#### The browser.UserContext Type ####

The <code>browser.ClientWindowInfo</code> type represents properties of a client window.

```cddl
browser.UserContext = text;
```


#### The browser.UserContextInfo Type ####

The <code><dfn>browser.UserContext</dfn></code> unique identifies a user context.

```cddl
browser.UserContextInfo = {
  userContext: browser.UserContext
}
```


### Commands ###


#### The browser.close Command ####

The <code>browser.UserContextInfo</code> type represents properties of a user context. The <dfn export for=commands>browser.close</dfn> command terminates all WebDriver sessions and cleans up automation state in the remote browser instance.

```cddl
browser.Close = (
        method: "browser.close",
        params: EmptyParams,
      )
```

```cddl
browser.CloseResult = EmptyResult
```


#### The browser.createUserContext Command ####

The <dfn export for=commands>browser.createUserContext</dfn> command creates a user context.

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


#### The browser.getClientWindows Command ####

The <dfn export for=commands>browser.getClientWindows</dfn> command returns a list of client windows.

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


#### The browser.getUserContexts Command ####

The <dfn export for=commands>browser.getUserContexts</dfn> command returns a list of user contexts.

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


#### The browser.removeUserContext Command ####

The <dfn export for=commands>browser.removeUserContext</dfn> command closes a user context and all navigables in it without running

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


#### The browser.setClientWindowState Command ####

The <dfn export for=commands>browser.setClientWindowState</dfn> command sets the dimensions of a client window.

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


#### The browser.setDownloadBehavior Command ####

A <dfn>download behavior struct</dfn> is a struct with: * struct/item named <dfn id="download-behavior-struct-allowed" for="download-behavior-struct">allowed</dfn> which is a boolean; * struct/item named <dfn id="download-behavior-struct-destination-folder" for="download-behavior-struct">destinationFolder</dfn> which is a string or null. A remote end has a <dfn>download behavior</dfn> which is a struct with an struct/item named <dfn for="download behavior">default download behavior</dfn>, which is a download behavior struct or null, and an struct/item named <dfn for="download behavior">user context download behavior</dfn>, which is a weak map between user context|user contexts and download behavior struct.

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


## The browsingContext Module ##


### Definition ###

The <dfn export for=modules>browsingContext</dfn> module contains commands and events relating to /navigables. rather than <code>navigable</code>, and the protocol uses the term and response parameters. The progress of navigation is communicated using an immutable struct canceled before making progress.</dd> "<dfn export id="navigation-status-canceled"><code>canceled</code></dfn>", "<dfn export id="navigation-status-pending"><code>pending</code></dfn>", or "<dfn export id="navigation-status-complete"><code>complete</code></dfn>". available, absolute filepath of the downloaded file, otherwise null.</dd> {^remote end definition^}

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

{^local end definition^}

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


### Types ###


#### The browsingContext.BrowsingContext Type ####

A remote end has a <dfn>device pixel ratio overrides</dfn> which is a weak map between /navigables and device pixel ratio overrides. It is initially empty. ratio overrides outlive any WebDriver session. A <dfn>viewport dimensions</dfn> is a struct with: * struct/Item named <dfn for="viewport-dimensions">height</dfn> which is an integer; * struct/Item named <dfn for="viewport-dimensions">width</dfn> which is an integer. A <dfn>viewport configuration</dfn> is a struct with: * struct/Item named <dfn for="viewport-configuration">viewport</dfn> which is a viewport dimensions or null; * struct/Item named <dfn for="viewport-configuration">devicePixelRatio</dfn> which is a float or null. An <dfn>unhandled prompt behavior struct</dfn> is a struct with: * struct/Item named <dfn attribute for="unhandled-prompt-behavior-alert">alert</dfn> which is a string or null; * struct/Item named <dfn attribute for="unhandled-prompt-behavior-beforeUnload">beforeUnload</dfn> which is a string or null; * struct/Item named <dfn attribute for="unhandled-prompt-behavior-confirm">confirm</dfn> which is a string or null; * struct/Item named <dfn attribute for="unhandled-prompt-behavior-default">default</dfn> which is a string or null; * struct/Item named <dfn attribute for="unhandled-prompt-behavior-file">file</dfn> which is a string or null; * struct/Item named <dfn attribute for="unhandled-prompt-behavior-prompt">prompt</dfn> which is a string or null. A remote end has a <dfn>viewport overrides map</dfn> which is a weak map between user context|user contexts and viewport configuration. A remote end has a <dfn>locale overrides map</dfn> which is a weak map between /navigables or user context|user contexts and string. A <dfn>screen settings</dfn> is a struct with an struct/item named an struct/item named <dfn attribute for="screen settings">width</dfn> which is an integer, an struct/item named <dfn attribute for="screen settings">x</dfn> which is an integer, an struct/item named <dfn attribute for="screen settings">y</dfn> which is an integer. A remote end has a <dfn>screen settings overrides</dfn> which is a struct with an struct/item named <dfn for="screen settings overrides">user context screen settings</dfn>, which is a weak map between user context|user contexts and screen settings, and an struct/item named <dfn for="screen settings overrides">navigable screen settings</dfn>, which is a weak map between /navigables and screen settings. A remote end has a <dfn>timezone overrides map</dfn> which is a weak map between /navigables or user context|user contexts and string. A remote end has an <dfn>unhandled prompt behavior overrides map</dfn> which is a weak map between user context|user contexts and unhandled prompt behavior struct. A remote end has a <dfn>scripting enabled overrides map</dfn> which is a weak map between /navigables or user context|user contexts and boolean. A remote end has a <dfn>download id map</dfn> which is is a weak map between response and download ids. It is initially empty. A <dfn>screencast stream</dfn> is an abstract stream of the viewport of a /top-level traversable, consisting of a <dfn for="screencast stream">video track</dfn> containing the rendered visual output of the /top-level traversable's document's viewport, and optionally an <dfn for="screencast stream">audio track</dfn> containing the audio output of the /top-level traversable's document. A BiDi session has a <dfn>screencast recordings map</dfn> which is a /map in which the keys are [[!RFC9562|UUID]]s, and the values are <dfn>screencast recording</dfn>, which is a struct with an struct/item named <dfn for="screencast recording">stream</dfn>, which is a screencast stream, an struct/item named <dfn for="screencast recording">path</dfn>, which is a string, an struct/item named <dfn for="screencast recording">state</dfn>, which is one of "<code>recording</code>", "<code>stopping</code>", "<code>stopped</code>", an struct/item named <dfn for="screencast recording">writeError</dfn>, which is a string or null. {^remote end definition^} and {^local end definition^}

```cddl
browsingContext.BrowsingContext = text;
```


#### The browsingContext.Info Type ####

Each /navigable has an associated <dfn export>navigable id</dfn>, which is a string uniquely identifying that navigable. This is implicitly set when the navigable is created. For navigables with an associated WebDriver window handle the /navigable id must be the same as the window handle. Each /navigable also has an <dfn>associated storage partition</dfn>, which is the storage partition it uses to persist data. Each /navigable also has an associated <dfn>original opener</dfn>, which is a /navigable that caused the navigable to open or null, initially set to null. {^local end definition^}

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


#### The browsingContext.Locator Type ####

The <code>browsingContext.Info</code> type represents the properties of a navigable. {^remote end definition^} and {^local end definition^}

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


#### The browsingContext.Navigation Type ####

The <code>browsingContext.Locator</code> type provides details on the strategy for locating a node in a document. {^remote end definition^} and {^local end definition^}

```cddl
browsingContext.Navigation = text;
```


#### The browsingContext.Download Type ####

The <code>browsingContext.Navigation</code> type is a unique string identifying an ongoing navigation. TODO: Link to the definition in the HTML spec. {^remote end definition^} and {^local end definition^}

```cddl
browsingContext.Download = text;
```


#### The browsingContext.NavigationInfo Type ####

The <code>browsingContext.Download</code> type is a unique string identifying a download. {^local end definition^}:

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


#### The browsingContext.ReadinessState Type ####

The <code>browsingContext.NavigationInfo</code> type provides details of an ongoing navigation.

```cddl
browsingContext.ReadinessState = "none" / "interactive" / "complete"
```


#### The browsingContext.UserPromptType Type ####

The <code>browsingContext.ReadinessState</code> type represents the stage of document loading at which a navigation command will return. {^Remote end definition^} and {^local end definition^}

```cddl
browsingContext.UserPromptType = "alert" / "beforeunload" / "confirm" / "prompt";
```


### Commands ###


#### The browsingContext.activate Command ####

The <code>browsingContext.UserPromptType</code> type represents the possible user prompt types. The <dfn export for=commands>browsingContext.activate</dfn> command activates and focuses the given /top-level traversable.

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


#### The browsingContext.captureScreenshot Command ####

The <dfn export for=commands>browsingContext.captureScreenshot</dfn> command captures an image of the given navigable, and returns it as a Base64-encoded string.

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


#### The browsingContext.close Command ####

The remote end steps with <var ignore>session</var> and |command parameters| are: 1. Let |navigable id| be the value of the <code>context</code> field of |command parameters| if present, or null otherwise. 1. Let |navigable| be the result of trying to get a navigable with |navigable id|. 1. If the implementation is unable to capture a screenshot of |navigable| for any reason then return error with error code unsupported operation. 1. Let |document| be |navigable|'s active document. 1. Immediately after the next invocation of the run the animation frame callbacks algorithm for |document|: Issue(w3c/webdriver-bidi#1131): This ought to be integrated into the update rendering algorithm in some more explicit way. 1. Let |origin| be the value of the <code>context</code> field of |command parameters| if present, or "viewport" otherwise. 1. Let |origin rect| be the result of trying to get the origin rectangle given |origin| and |document|. 1. Let |clip rect| be |origin rect|. 1. If |command parameters| contains "<code>clip</code>": 1. Let |clip| be |command parameters|["<code>clip</code>"]. 1. Run the steps under the first matching condition: production: 1. Let |environment settings| be the environment settings object whose relevant global object's associated <code>Document</code> is |document|. 1. Let |realm| be |environment settings|' realm execution context's Realm component. 1. Let |element| be the result of trying to deserialize remote reference with |clip|["<code>element</code>"], |realm|, and |session|. 1. If |element| doesn't implement Element return error with error code no such element. 1. If |element|'s node document is not |document|, return error with error code no such element. 1. Let |viewport rect| be get the origin rectangle given "<code>viewport</code>" and |document|. 1. Let |element rect| be get the bounding box for |element|. 1. Let |clip rect| be a DOMRectReadOnly with x coordinate |element rect|["<code>x</code>"] + |viewport rect|["<code>x</code>"], y coordinate |element rect|["<code>y</code>"] + |viewport rect|["<code>y</code>"], width |element rect|["<code>width</code>"], and height |element rect|["<code>height</code>"]. 1. Let |clip x| be |clip|["<code>x</code>"] plus |origin rect|'s x coordinate. 1. Let |clip y| be |clip|["<code>y</code>"] plus |origin rect|'s y coordinate. 1. Let |clip rect| be a DOMRectReadOnly with x coordinate |clip x|, y coordinate |clip y|, width |clip|["<code>width</code>"], and height |clip|["<code>height</code>"]. 1. Note: All coordinates are now measured from the origin of the document. 1. Let |rect| be the rectangle intersection of |origin rect| and |clip rect|. 1. If |rect|'s width dimension is 0 or |rect|'s height dimension is 0, return error with error code unable to capture screen. 1. Let |canvas| be render document to a canvas with |document| and |rect|. 1. Let |format| be the <code>format</code> field of |command parameters|. 1. Let |encoding result| be the result of trying to encode a canvas as Base64 with |canvas| and |format|. 1. Let |body| be a /map matching the 1. Return success with data |body|. The <dfn export for=commands>browsingContext.close</dfn> command closes a /top-level traversable.

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


#### The browsingContext.create Command ####

The <dfn export for=commands>browsingContext.create</dfn> command creates a new /navigable, either in a new tab or in a new window, and returns its navigable id.

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


#### The browsingContext.getTree Command ####

The <dfn export for=commands>browsingContext.getTree</dfn> command returns a tree of all descendent navigables including the given parent itself, or all top-level contexts when no parent is provided.

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


#### The browsingContext.handleUserPrompt Command ####

The <dfn export for=commands>browsingContext.handleUserPrompt</dfn> command allows closing an open prompt

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


#### The browsingContext.locateNodes Command ####

The <dfn export for=commands>browsingContext.locateNodes</dfn> command returns a list of all nodes matching the specified locator.

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


#### The browsingContext.navigate Command ####

The <dfn export for=commands>browsingContext.navigate</dfn> command navigates a navigable to the given URL.

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


#### The browsingContext.print Command ####

The <dfn export for=commands>browsingContext.print</dfn> command creates a paginated representation of a document, and returns it as a PDF document represented as a Base64-encoded string.

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


#### The browsingContext.reload Command ####

The <dfn export for=commands>browsingContext.reload</dfn> command reloads a navigable.

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


#### The browsingContext.setBypassCSP Command ####

The <dfn export for=commands>browsingContext.setBypassCSP</dfn> command allows bypassing Content Security Policy enforcement.

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


#### The browsingContext.setViewport Command ####

A remote end has a <dfn>bypass CSP configuration</dfn>, which is WebDriver configuration with WebDriver configuration/associated type boolean. The <dfn export for=commands>browsingContext.setViewport</dfn> command modifies specific viewport characteristics (e.g. viewport width and viewport height) on the given top-level traversable.

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


#### The browsingContext.startScreencast Command ####

The <dfn export for=commands>browsingContext.startScreencast</dfn> command starts the screencast of a given navigable and writes it to a file. Cleaning up the file is left to the local end. In some configurations this might not be possible — for example, if the remote end has read/write access to the filesystem but the local end has only read-only access.

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


#### The browsingContext.stopScreencast Command ####

The <dfn export for=commands>browsingContext.stopScreencast</dfn> command stops the screencast.

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


#### The browsingContext.traverseHistory Command ####

The <dfn export for=commands>browsingContext.traverseHistory</dfn> command traverses the history of a given navigable by a delta.

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


### Events ###


#### The browsingContext.contextCreated Event ####

```cddl
browsingContext.ContextCreated = (
         method: "browsingContext.contextCreated",
         params: browsingContext.Info
        )
```


#### The browsingContext.contextDestroyed Event ####

```cddl
browsingContext.ContextDestroyed = (
         method: "browsingContext.contextDestroyed",
         params: browsingContext.Info
        )
```


#### The browsingContext.navigationStarted Event ####

The remote end event trigger is:

```cddl
browsingContext.NavigationStarted = (
         method: "browsingContext.navigationStarted",
         params: browsingContext.NavigationInfo
        )
```


#### The browsingContext.fragmentNavigated Event ####

```cddl
browsingContext.FragmentNavigated = (
         method: "browsingContext.fragmentNavigated",
         params: browsingContext.NavigationInfo
        )
```


#### The browsingContext.historyUpdated Event ####

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


#### The browsingContext.domContentLoaded Event ####

```cddl
browsingContext.DomContentLoaded = (
         method: "browsingContext.domContentLoaded",
         params: browsingContext.NavigationInfo
        )
```


#### The browsingContext.load Event ####

```cddl
browsingContext.Load = (
         method: "browsingContext.load",
         params: browsingContext.NavigationInfo
        )
```


#### The browsingContext.downloadWillBegin Event ####

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


#### The browsingContext.downloadEnd Event ####

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


#### The browsingContext.navigationAborted Event ####

```cddl
browsingContext.NavigationAborted = (
         method: "browsingContext.navigationAborted",
         params: browsingContext.NavigationInfo
        )
```


#### The browsingContext.navigationCommitted Event ####

```cddl
browsingContext.NavigationCommitted = (
         method: "browsingContext.navigationCommitted",
         params: browsingContext.NavigationInfo
        )
```


#### The browsingContext.navigationFailed Event ####

```cddl
browsingContext.NavigationFailed = (
         method: "browsingContext.navigationFailed",
         params: browsingContext.NavigationInfo
        )
```


#### The browsingContext.userPromptClosed Event ####

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


#### The browsingContext.userPromptOpened Event ####

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


## The emulation Module ##


### Definition ###

The <dfn export for=modules>emulation</dfn> module contains commands and events relating to emulation of browser APIs. {^remote end definition^}

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


### Commands ###


#### The emulation.setForcedColorsModeThemeOverride Command ####

A BiDi session has an <dfn for=session>emulated user agent</dfn> which is a struct with an struct/item named an struct/item named between user context|user contexts and string, and an struct/item named between /navigables and string. A BiDi session has <dfn for=session>emulated maxTouchPoints</dfn>, which is a struct with an struct/item named <dfn for="emulated maxTouchPoints">default</dfn>, which is an integer or null, initially null; an struct/item named <dfn for="emulated maxTouchPoints">user contexts</dfn>, which is a weak map between user context|user contexts and integer, initially empty; and an struct/item named <dfn for="emulated maxTouchPoints">navigables</dfn>, which is a weak map between /navigables and integer, initially empty. A <dfn>screen orientation override</dfn> is a struct with: * struct/item named <dfn attribute for="screen orientation override">natural</dfn> which is a string; * struct/item named <dfn attribute for="screen orientation override">type</dfn> which is a string; A remote end has a <dfn>screen orientation overrides map</dfn> which is a weak map between user context|user contexts and screen orientation override. The <dfn export for=commands>emulation.setForcedColorsModeThemeOverride</dfn> command modifies forced colors mode theming characteristics on the given top-level traversables or user contexts.

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


#### The emulation.setGeolocationOverride Command ####

A remote end has a <dfn>forced colors mode theme override configuration</dfn>, which is WebDriver configuration with WebDriver configuration/associated type string. The <dfn export for=commands>emulation.setGeolocationOverride</dfn> command modifies geolocation characteristics on the given top-level traversables or user contexts.

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


#### The emulation.setLocaleOverride Command ####

A <dfn>geolocation override</dfn> is a struct with: * struct/item named <dfn attribute for="geolocation override">latitude</dfn> which is a float; * struct/item named <dfn attribute for="geolocation override">longitude</dfn> which is a float; * struct/item named <dfn attribute for="geolocation override">accuracy</dfn> which is a float; * struct/item named <dfn attribute for="geolocation override">altitude</dfn> which is a float or null; * struct/item named <dfn attribute for="geolocation override">altitudeAccuracy</dfn> which is a float or null; * struct/item named <dfn attribute for="geolocation override">heading</dfn> which is a float or null; * struct/item named <dfn attribute for="geolocation override">speed</dfn> which is a float or null. A remote end has a <dfn>geolocation override configuration</dfn>, which is WebDriver configuration with WebDriver configuration/associated type geolocation override. The <dfn export for=commands>emulation.setLocaleOverride</dfn> command modifies locale on the given top-level traversables or user contexts.

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


#### The emulation.setMediaFeaturesOverride Command ####

The <dfn export for=commands>emulation.setMediaFeaturesOverride</dfn> command allows overriding the values of various media features.

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


#### The emulation.setNetworkConditions Command ####

A remote end has a <dfn>media features override configuration</dfn>, which is WebDriver configuration with WebDriver configuration/associated type /map. The <dfn export for=commands>emulation.setNetworkConditions</dfn> command emulates specific network conditions for the given browsing context or for a user context.

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


#### The emulation.setScreenSettingsOverride Command ####

The <dfn export for=commands>emulation.setScreenSettingsOverride</dfn> command emulates web-exposed screen area and web-exposed available screen area of the given top-level traversables or user contexts.

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


#### The emulation.setScreenOrientationOverride Command ####

The <dfn export for=commands>emulation.setScreenOrientationOverride</dfn> command emulates screen orientation of the given top-level traversables or user contexts.

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


#### The emulation.setUserAgentOverride Command ####

The <dfn export for=commands>emulation.setUserAgentOverride</dfn> command modifies User-Agent on the given top-level traversables, user contexts, or globally.

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


#### The emulation.setViewportMetaOverride Command ####

The <dfn export for=commands>emulation.setViewportMetaOverride</dfn> command modifies whether the browser respects the <code>&lt;meta name=viewport&gt;</code> tag.

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


#### The emulation.setScriptingEnabled Command ####

A remote end has a <dfn>viewport meta override configuration</dfn>, which is WebDriver configuration with WebDriver configuration/associated type boolean. The <dfn export for=commands>emulation.setScriptingEnabled</dfn> command emulates disabling JavaScript on web pages.

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


#### The emulation.setScrollbarTypeOverride Command ####

The <dfn export for=commands>emulation.setScrollbarTypeOverride</dfn> command modifies scrollbar type on the given top-level traversables, user contexts or globally.

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


#### The emulation.setTimezoneOverride Command ####

A remote end has a <dfn>scrollbar type override configuration</dfn>, which is WebDriver configuration with WebDriver configuration/associated type string. The <dfn export for=commands>emulation.setTimezoneOverride</dfn> command modifies timezone on the given top-level traversables or user contexts.

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


#### The emulation.setTouchOverride Command ####

The <dfn export for=commands>emulation.setTouchOverride</dfn> command emulates enabled touch input on web pages.

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


## The network Module ##


### Definition ###

The <dfn export for=modules>network</dfn> module contains commands and events relating to network requests. {^remote end definition^}

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

{^local end definition^}

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


### Network Data Collection ###


### Network Intercepts ###


### Types ###


#### The network.AuthChallenge Type ####

A remote end has a <dfn>before request sent map</dfn> which is initially an empty map.  It's used to track the network events for which a A remote end has a <dfn>default cache behavior</dfn> which is a string. It is initially "<code>default</code>". A remote end has a <dfn>navigable cache behavior map</dfn> which is a weak map between /top-level traversables and strings representing cache behavior. It is initially empty. A BiDi session has a <dfn for=session>extra headers</dfn> which is a struct with an struct/item named <dfn for="extra headers">default headers</dfn>, which is a /header list (initially set to an empty /header list), an struct/item named between user context|user contexts and /header lists, and  a struct/item named between /navigables and /header lists. A <dfn>network data</dfn> is a /struct with: * struct/Item named <dfn for="network-data">bytes</dfn>, which is a <code>network.BytesValue</code> or null, * struct/Item named <dfn for="network-data">cloned body</dfn>, which is a /body or null, * struct/Item named <dfn for="network-data">collectors</dfn>, which is a list of <code>network.Collector</code>, * struct/Item named <dfn for="network-data">pending</dfn>, which is a boolean, * struct/Item named <dfn for="network-data">request</dfn>, which is a request id, * struct/Item named <dfn for="network-data">size</dfn>, which is a js-uint or null, * struct/Item named <dfn for="network-data">type</dfn>, which is a <code>network.DataType</code>. A <dfn for="network">collector</dfn> is a /struct with: * struct/Item named <dfn for="network-collector">max encoded item size</dfn>, which is a js-uint; * struct/item named <dfn for="network-collector">contexts</dfn>, which is a /list of navigable id; * struct/item named <dfn for="network-collector">data types</dfn>, which is a /list of  <code>network.DataType</code>; * struct/item named <dfn for="network-collector">collector</dfn>, which is a <code>network.Collector</code>; * struct/item named <dfn for="network-collector">collector type</dfn>, which is a <code>network.CollectorType</code>; * struct/item named <dfn for="network-collector">user contexts</dfn>, which is a /list of <code>browser.UserContext</code>. and does not limit the size collected by the specific collector. The total size of all collected resources is limited by max total collected size. A BiDi session has <dfn>network collectors</dfn> which is a /map between A remote end has <dfn>collected network data</dfn> which is a list of network data. It is initially empty. A remote end has a <dfn>max total collected size</dfn> which is a js-uint representing the size allocated to collect network data in collected network data. Its value is implementation-defined. It is expected that the limits are sufficiently large that users can depend on collecting data that is fully decoded and handled by the browser, such as images and fonts used on a webpage. A <dfn>network intercept</dfn> is a mechanism to allow remote ends to intercept and modify network requests and responses. A BiDi session has an <dfn>intercept map</dfn> which is a /map between intercept id and a struct with fields <code>url patterns</code>, of active network intercepts. It is initially empty. A BiDi session has a <dfn>blocked request map</dfn>, used to track the requests which are actively being blocked. It is an /map between request id and a struct with fields <code>request</code>, <code>phase</code>, and

```cddl
network.AuthChallenge = {
  scheme: text,
  realm: text,
}
```


#### The network.AuthCredentials Type ####

```cddl
network.AuthCredentials = {
  type: "password",
  username: text,
  password: text,
}
```


#### The network.BaseParameters Type ####

The <code>network.AuthCredentials</code> type represents the response to a request for authorization credentials.

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


#### The network.BytesValue Type ####

The <code>network.BaseParameters</code> type is an abstract type representing the data that's common to all network events. Issue: Consider including the `sharedId` of the document node that initiated the request in addition to the context.

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


#### The network.Collector Type ####

The <code><dfn>network.BytesValue</dfn></code> type represents binary data sent over the network. Valid UTF-8 is represented with the <code>network.StringValue</code> type, any other data is represented in Base64-encoded form as {^Remote end definition^} and {^local end definition^}

```cddl
network.Collector = text
```


#### The network.CollectorType Type ####

The <code><dfn>network.Collector</dfn></code> type represents the id of a network/collector. {^Remote end definition^} and {^local end definition^}

```cddl
network.CollectorType = "blob"
```


#### The network.Cookie Type ####

which want to read the data gathered by a given collector via a stream. The <code><dfn>network.CollectorType</dfn></code> type represents the different types of data collectors that can be added. {^Remote end definition^} and {^local end definition^}

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


#### The network.CookieHeader Type ####

The <code>network.Cookie</code> type represents a cookie. {^Remote end definition^}

```cddl
network.CookieHeader = {
    name: text,
    value: network.BytesValue,
}
```


#### The network.DataType Type ####

The <code>network.CookieHeader</code> type represents the subset of cookie data that's in a <code>Cookie</code> request header. {^Remote end definition^} and {^local end definition^}

```cddl
network.DataType = "request" / "response"
```


#### The network.FetchTimingInfo Type ####

The <code><dfn>network.DataType</dfn></code> type represents the different types of network data that can be collected. {^Remote end definition^} and {^local end definition^}

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


#### The network.Header Type ####

The <code>network.FetchTimingInfo</code> type represents the time of each part of the request, relative to the time origin of the /request's request/client. TODO: Add service worker fields {^Remote end definition^} and {^local end definition^}

```cddl
network.Header = {
  name: text,
  value: network.BytesValue,
}
```


#### The network.Initiator Type ####

The <code>network.Header</code> type represents a single request header. {^Remote end definition^} and {^local end definition^}

```cddl
network.Initiator = {
    ? columnNumber: js-uint,
    ? lineNumber: js-uint,
    ? request: network.Request,
    ? stackTrace: script.StackTrace,
    ? type: "parser" / "script" / "preflight" / "other"
}
```


#### The network.Intercept Type ####

The <code>network.Initiator</code> type represents the source of a network request. compatibility, but is no longer set by the get the initiator steps, and will be removed in a future revision of this specification. Its use is expected to be replaced by <code>initiatorType</code> and <code>destination</code> on compatibility, but is no longer set by the get the initiator steps, and will be removed in a future revision of this specification. The request id, making this information redundant. See [[#type-network-BaseParameters]]. {^Remote end definition^} and {^local end definition^}

```cddl
network.Intercept = text
```


#### The network.Request Type ####

The <code>network.Intercept</code> type represents the id of a network intercept. {^Remote end definition^} and {^local end definition^}

```cddl
network.Request = text;
```


#### The network.RequestData Type ####

Each network request has an associated <dfn export>request id</dfn>, which is a string uniquely identifying that request. The identifier for a request resulting from a redirect matches that of the request that initiated it. {^Remote end definition^} and {^local end definition^}

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


#### The network.ResponseContent Type ####

The <code>network.RequestData</code> type represents an ongoing network request. {^Remote end definition^} and {^local end definition^}

```cddl
network.ResponseContent = {
    size: js-uint
}
```


#### The network.ResponseData Type ####

The <code>network.ResponseContent</code> type represents the decoded response to a network request. would be natural to add a field here if we have a way to return the body --> {^Remote end definition^} and {^local end definition^}

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


#### The network.SetCookieHeader Type ####

The <code>network.ResponseData</code> type represents the response to a network request. {^Remote end definition^}

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


#### The network.UrlPattern Type ####

The <code>network.SetCookieHeader</code> represents the data in a {^Remote end definition^}

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


### Commands ###


#### The network.addDataCollector Command ####

A <code>network.UrlPattern</code> represents a pattern used for matching request URLs for network intercepts. When URLs are matched against a <code>network.UrlPattern</code> the URL is parsed, and each component is compared for equality with the corresponding field in the pattern, if present. Missing fields from the pattern always match. the syntax forbids characters that are treated specially in the [[URLPattern]] specification. These can be escaped by prefixing them with a U+005C (\) character. The <dfn export for=commands>network.addDataCollector</dfn> adds a network/collector.

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


#### The network.addIntercept Command ####

The <dfn export for=commands>network.addIntercept</dfn> command adds a network intercept.

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


#### The network.continueRequest Command ####

The <dfn export for=commands>network.continueRequest</dfn> command continues a request that's blocked by a network intercept.

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


#### The network.continueResponse Command ####

The <dfn export for=commands>network.continueResponse</dfn> command continues a response that's blocked by a network intercept. It can be called in the response, but still provide the network response body.

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


#### The network.continueWithAuth Command ####

The <dfn export for=commands>network.continueWithAuth</dfn> command continues a response that's blocked by a network intercept at the

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


#### The network.disownData Command ####

The <dfn export for=commands>network.disownData</dfn> command releases a collected network data for a given network/collector.

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


#### The network.failRequest Command ####

The <dfn export for=commands>network.failRequest</dfn> command fails a fetch that's blocked by a network intercept.

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


#### The network.getData Command ####

The <dfn export for=commands>network.getData</dfn> command retrieves a network data if it is available.

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


#### The network.provideResponse Command ####

The <dfn export for=commands>network.provideResponse</dfn> command continues a request that's blocked by a network intercept, by providing a complete response. lifecycle, and therefore emitting other events as it progresses.

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


#### The network.removeDataCollector Command ####

The <dfn export for=commands>network.removeDataCollector</dfn> command removes a network/collector.

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


#### The network.removeIntercept Command ####

The <dfn export for=commands>network.removeIntercept</dfn> command removes a network intercept.

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


#### The network.setCacheBehavior Command ####

The <dfn export for=commands>network.setCacheBehavior</dfn> command configures the network cache behavior for certain requests.

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


#### The network.setExtraHeaders Command ####

The <dfn export for=commands>network.setExtraHeaders</dfn> command allows specifying headers that will extend, or overwrite, existing request headers.

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


### Events ###


#### The network.authRequired Event ####

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


#### The network.beforeRequestSent Event ####

This event is emitted when the user agent is going to prompt for authorization credentials.

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


#### The network.fetchError Event ####

This event is emitted before a request is sent (either over the network or before it's handled by a serviceworker or a local cache).

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


#### The network.responseCompleted Event ####

This event is emitted when a network request ends in an error.

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


#### The network.responseStarted Event ####

This event is emitted after the full response body is received.

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


## The script Module ##


### Definition ###

This event is emitted after the response headers are received but before the body is complete. The <dfn export for=modules>script</dfn> module contains commands and events relating to script realms and execution. {^Remote end definition^}

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

{^local end definition^}

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


### Preload Scripts ###


### Types ###


#### The script.Channel Type ####

A <dfn>Preload script</dfn> is one which runs on creation of a new Window, before any author-defined script have run. TODO: Extend this to scripts in other kinds of realms. A BiDi session has a <dfn>preload script map</dfn> which is a /map in which the keys are [[!RFC9562|UUID]]s, and the values are structs with an struct/item named <code>function declaration</code>, which is a string, an struct/item named <code>arguments</code>, which is a list, an struct/item named <code>contexts</code>, which is a list or null, an struct/item named <code>sandbox</code>, which is a string or null, and an struct/item named <code>user contexts</code>, which is a /set. a runtime exception, an [[ECMAScript]] exception is reported in the realm in which it was being executed, and other preload scripts run as normal. {^Remote end definition^} and {^local end definition^}

```cddl
script.Channel = text;
```


#### The script.ChannelValue Type ####

The <code><dfn>script.Channel</dfn></code> type represents the id of a specific channel used to send custom messages from the remote end to the local end. {^Remote end definition^}

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


#### The script.EvaluateResult Type ####

The <code>script.ChannelValue</code> type represents an messages from the remote end to the local end. {^Remote end definition^} and {^local end definition^}

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


#### The script.ExceptionDetails Type ####

The <code>script.EvaluateResult</code> type indicates the return value of a command that executes script. The <code>script.EvaluateResultSuccess</code> variant is used in cases where the script completes normally and the completes with a thrown exception. {^Remote end definition^} and {^local end definition^}

```cddl
script.ExceptionDetails = {
  columnNumber: js-uint,
  exception: script.RemoteValue,
  lineNumber: js-uint,
  stackTrace: script.StackTrace,
  text: text,
}
```


#### The script.Handle Type ####

The <code>script.ExceptionDetails</code> type represents a JavaScript exception. {^Remote end definition^} and {^local end definition^}

```cddl
script.Handle = text;
```


#### The script.InternalId Type ####

The <code>script.Handle</code> type represents a handle to an object owned by the ECMAScript runtime. The handle is only valid in a specific Realm. Each ECMAScript Realm has a corresponding <dfn>handle object map</dfn>. This is a strong /map from handle ids to their corresponding objects. {^Remote end definition^} and {^local end definition^}

```cddl
script.InternalId = text;
```


#### The script.LocalValue Type ####

The <code>script.InternalId</code> type represents the id of a previously serialized <code>script.RemoteValue</code> during serialize as a remote value|serialization. {^Remote end definition^}

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


#### The script.PreloadScript Type ####

The <code><dfn export>script.LocalValue</dfn></code> type represents values which can be deserialized into ECMAScript. This includes both primitive and non-primitive values as well as script.RemoteReference|remote references and script.Channel|channels. {^Remote end definition^} and {^local end definition^}

```cddl
script.PreloadScript = text;
```


#### The script.Realm Type ####

The <code>script.PreloadScript</code> type represents a handle to a script that will run on realm creation. {^Remote end definition^} and {^local end definition^}

```cddl
script.Realm = text;
```


#### The script.PrimitiveProtocolValue Type ####

Each realm has an associated <dfn export>realm id</dfn>, which is a string uniquely identifying that realm. This is implicitly set when the realm is created. The realm id for a realm is opaque and must not be derivable from the handle id of the corresponding global object in the handle object map or, where relevant, from the navigable id of any /navigable. relationships between different ids. {^Remote end definition^} and {^local end definition^}

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


#### The script.RealmInfo Type ####

The <dfn>script.PrimitiveProtocolValue</dfn> represents values which can only be represented by value, never by reference. {^Local end definition^}

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


#### The script.RealmType Type ####

variants and values of <code>script.RealmType</code>. The <code>script.RealmInfo</code> type represents the properties of a realm. {^Remote end definition^} and {^local end definition^}

```cddl
script.RealmType = "window" / "dedicated-worker" / "shared-worker" / "service-worker" /
                   "worker" / "paint-worklet" / "audio-worklet" / "worklet"
```


#### The script.RemoteReference Type ####

The <code>script.RealmType</code> type represents the different types of Realm. {^Remote end definition^}

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


#### The script.RemoteValue Type ####

The <code><dfn>script.RemoteReference</dfn></code> type is either a existing ECMAScript object in handle object map in the given Realm, or is a <code>script.SharedReference</code> representing a reference to a node. Issue: handle "stale object reference" case. only <code>sharedId</code>. {^Remote end definition^} and {^local end definition^}

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


#### The script.ResultOwnership Type ####

Issue: Add WASM types? Issue: Should WindowProxy get attributes in a similar style to Node? Issue: handle String / Number / etc. wrapper objects specially? Values accessible from the ECMAScript runtime are represented by a mirror object, specified as <code>script.RemoteValue</code>. The value's type is specified in the <code>type</code> property. In the case of JSON-representable primitive values, this contains the value in the <code>value</code> property; in the case of non-JSON-representable primitives, the <code>value</code> property contains a string representation of the value. For non-primitive objects, the <code>handle</code> property, when present, contains a unique string handle to the object. The handle is unique for each serialization. The remote end will keep objects with a corresponding handle alive until such a time that <code>script.disown</code> is called with that handle, or the realm itself is to be discarded (e.g. due to navigation). For some non-primitive types, the <code>value</code> property contains a representation of the data in the ECMAScript object; for container types this can contain further <code>script.RemoteValue</code> instances. The object i.e. the object has already been serialized in the current the maximum serialization depth is reached. In case of duplicated objects in the same <code>script.RemoteValue</code>, the value is provided only for one of the remote values, while the unique-per-ECMAScript-object <code>internalId</code> is provided for all the duplicated objects for a given serialization. Nodes are also represented by <code>script.RemoteValue</code> instances. These have a partial serialization of the node in the value property. Issue: reconsider mirror objects' lifecycle. object is discarded in the runtime, subsequent attempts to access it via the protocol will result in an error.

```cddl
script.ResultOwnership = "root" / "none"
```


#### The script.SerializationOptions Type ####

The <code>script.ResultOwnership</code> specifies how the serialized value ownership will be treated. {^Remote end definition^}

```cddl
script.SerializationOptions = {
  ? maxDomDepth: (js-uint / null) .default 0,
  ? maxObjectDepth: (js-uint / null) .default null,
  ? includeShadowTree: ("none" / "open" / "all") .default "none",
}
```


#### The script.SharedId Type ####

The <code>script.SerializationOptions</code> allows specifying how ECMAScript objects will be serialized. {^Remote end definition^} and {^local end definition^}

```cddl
script.SharedId = text;
```


#### The script.StackFrame Type ####

The <code>script.SharedId</code> type represents a reference to a DOM Node that is usable in any realm (including Sandbox Realms). {^Remote end definition^} and {^local end definition^}

```cddl
script.StackFrame = {
  columnNumber: js-uint,
  functionName: text,
  lineNumber: js-uint,
  url: text,
}
```


#### The script.StackTrace Type ####

A frame in a stack trace is represented by a <code>StackFrame</code> object. This has a <code>url</code> property, which represents the URL of the script, a <code>functionName</code> property which represents the name of the executing function, and <code>lineNumber</code> and <code>columnNumber</code> properties, which represent the line and column number of the executed code. {^Remote end definition^} and {^local end definition^}

```cddl
script.StackTrace = {
  callFrames: [*script.StackFrame],
}
```


#### The script.Source Type ####

The <code>script.StackTrace</code> type represents the javascript stack at a point in script execution. that list are underspecified, and therefore the details here are implementation defined. It is assumed that an implementation is able to generate a <dfn>list of stack frames</dfn>, which is a list with one entry for each item in the javascript call stack, starting from the most recent. Each entry is a single <dfn>stack frame</dfn> corresponding to execution of a statement or expression in a script |script|, which contains the following fields: of the resource containing |script|. the line in the resource containing |script|. The <dfn>current stack trace</dfn> is the result of construct a stack trace given a list of stack frames representing the callstack of the running execution context. {^Local end definition^}

```cddl
script.Source = {
  realm: script.Realm,
  ? context: browsingContext.BrowsingContext,
  ? userContext: browser.UserContext
}
```


#### The script.Target Type ####

The <code>script.Source</code> type represents a <code>script.Realm</code> with an optional <code>browsingContext.BrowsingContext</code> and related {^Remote end definition^}

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


### Commands ###


#### The script.addPreloadScript Command ####

The <code>script.Target</code> type represents a value that is either a This is useful in cases where a navigable identifier can stand in for the realm associated with the navigable's active document. The <dfn export for=commands>script.addPreloadScript</dfn> command adds a preload script.

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


#### The script.disown Command ####

The <dfn export for=commands>script.disown</dfn> command disowns the given handles. This does not guarantee the handled object will be garbage collected, as there can be other handles or strong ECMAScript references.

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


#### The script.callFunction Command ####

The <dfn export for=commands>script.callFunction</dfn> command calls a provided function with given arguments in a given realm.

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


#### The script.evaluate Command ####

Issue: TODO: Add timeout argument as described in the script.evaluate. The <dfn export for=commands>script.evaluate</dfn> command evaluates a provided script in a given realm. For convenience a navigable can be provided in place of a realm, in which case the realm used is the realm of the browsing context's active document. The method returns the value of executing the provided script, unless it returns a promise and <code>awaitPromise</code> is true, in which case the resolved value of the promise is returned.

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


#### The script.getRealms Command ####

script.EvaluateResult TODO: Add timeout argument. It's not totally clear how this ought to work; in Chrome it seems like the timeout doesn't apply to the promise resolve step, but that likely isn't what clients want. The <dfn export for=commands>script.getRealms</dfn> command returns a list of all realms, optionally filtered to realms of a specific type, or to the realm associated with a /navigable's active document.

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


#### The script.removePreloadScript Command ####

The <dfn export for=commands>script.removePreloadScript</dfn> command removes a preload script.

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


### Events ###


#### The script.message Event ####

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


#### The script.realmCreated Event ####

```cddl
script.RealmCreated = (
         method: "script.realmCreated",
         params: script.RealmInfo
        )
```


#### The script.realmDestroyed Event ####

The remote end event trigger is:

```cddl
script.RealmDestroyed = (
         method: "script.realmDestroyed",
         params: script.RealmDestroyedParameters
       )

       script.RealmDestroyedParameters = {
         realm: script.Realm
       }
```


## The storage Module ##


### Definition ###

The remote end event trigger is: The <dfn export for=modules>storage</dfn> module contains functionality and events related to storage. A <dfn>storage partition</dfn> is a namespace within which the user agent may organize persistent data such as cookies and local storage. A <dfn>storage partition key</dfn> is a /map which uniquely identifies a storage partition. {^Remote end definition^}

```cddl
StorageCommand = (
  storage.DeleteCookies //
  storage.GetCookies //
  storage.SetCookie
)
```

{^Local end definition^}

```cddl
StorageResult = (
  storage.DeleteCookiesResult /
  storage.GetCookiesResult /
  storage.SetCookieResult
)
```


### Types ###


#### The storage.PartitionKey Type ####

{^Local end definition^}

```cddl
storage.PartitionKey = {
  ? userContext: text,
  ? sourceOrigin: text,
  Extensible,
}
```


### Commands ###


#### The storage.getCookies Command ####

The <code>storage.PartitionKey</code> type represents a storage partition key. The following <dfn>table of standard storage partition key attributes</dfn> enumerates attributes with well-known meanings which a remote end may choose to support. An implementation may define additional extension storage partition key attributes. Remote ends may support any number of <dfn>extension storage partition key attributes</dfn>. In order to avoid conflicts with other implementations, these attributes must begin with a unique identifier for the vendor and user-agent followed by U+003A (:). A remote end has a /map of <dfn>default values for storage partition key attributes</dfn> which contains zero or more entries. Each key must be a member of the table of standard storage partition key attributes where the storage partition key corresponds to a standard storage partition, or an extension storage partition key attribute where it does not, and the values represent the default value of that partition key that will be used when the user doesn't provide an explicit value. The precise entries are implementation-defined and are determined by the storage partitioning adopted by the implementation. A remote end has a /list of <dfn>required partition key attributes</dfn> which contains zero or more entries. Each key must be a member of the table of standard storage partition key attributes where the storage partition key corresponds to a standard storage partition, or an extension storage partition key attribute where it does not. The precise entries are implementation-defined and are determined by the storage partitioning adopted by the implementation. This list includes only partition keys for which no default is available. As such the list must not share any entries with the keys of default values for storage partition key attributes. The <dfn export for=commands>storage.getCookies</dfn> command retrieves zero or more cookies which match cookie|match a set of provided parameters.

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


#### The storage.setCookie Command ####

The <dfn export for=commands>storage.setCookie</dfn> command creates a new cookie in a cookie store, replacing any cookie in that store which matches according to [[COOKIES]].

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


#### The storage.deleteCookies Command ####

The <dfn export for=commands>storage.deleteCookies</dfn> command removes zero or more cookies which match cookie|match a set of provided parameters.

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


## The log Module ##


### Definition ###

The <dfn export for=modules>log</dfn> module contains functionality and events related to logging. A BiDi Session has a <dfn>log event buffer</dfn> which is a /map from navigable id to a list of log events for that context that have not been emitted. User agents may impose a maximum size on this buffer, subject to the condition that if events A and B happen in the same context with A occurring before B, and both are added to the buffer, the entry for B must not be removed before the entry for A. {^Local end definition^}

```cddl
LogEvent = (
  log.EntryAdded
)
```


### Types ###


#### log.LogEntry ####

{^Local end definition^}

```cddl
log.Level = "debug" / "info" / "warn" / "error"

log.Entry = (
  log.GenericLogEntry /
  log.ConsoleLogEntry /
  log.JavascriptLogEntry
)

log.BaseLogEntry = (
  level: log.Level,
  source: script.Source,
  text: text / null,
  timestamp: js-uint,
  ? stackTrace: script.StackTrace,
)

log.GenericLogEntry = {
  log.BaseLogEntry,
  type: text,
}

log.ConsoleLogEntry = {
  log.BaseLogEntry,
  type: "console",
  method: text,
  args: [*script.RemoteValue],
}

log.JavascriptLogEntry = {
  log.BaseLogEntry,
  type: "javascript",
}
```


### Events ###


#### The log.entryAdded Event ####

Each log event is represented by a <code>log.Entry</code> object. This has a property representing the origin of the log entry, a <code>text</code> property with the log message string itself, and a <code>timestamp</code> property corresponding to the time the log entry was generated. Specific variants of the provide additional fields specific to the entry type.

```cddl
log.EntryAdded = (
         method: "log.entryAdded",
         params: log.Entry,
        )
```


## The input Module ##


### Definition ###

The remote end event trigger is: The <dfn export for=modules>input</dfn> module contains functionality for simulated user input. {^remote end definition^}

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

{^local end definition^}

```cddl
InputEvent = (
  input.FileDialogOpened
)
```


### Types ###


#### input.ElementOrigin ####

The <code>input.ElementOrigin</code> type represents an Element that will be used as a coordinate origin.

```cddl
input.ElementOrigin = {
  type: "element",
  element: script.SharedReference
}
```


### Commands ###


#### The input.performActions Command ####

The <dfn export for=commands>input.performActions</dfn> command performs a specified sequence of user input actions. actions section of [[WEBDRIVER]].

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


#### The input.releaseActions Command ####

The <dfn export for=commands>input.releaseActions</dfn> command resets the input state associated with the current session.

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


#### The input.setFiles Command ####

The <dfn export for=commands>input.setFiles</dfn> command sets the <code>files</code> property of a given <code>input</code> element with type <code>file</code> to a set of file paths.

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


### Events ###


#### The input.fileDialogOpened Event ####

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


## The webExtension Module ##


### Definition ###

A <dfn>WebDriver BiDi file picker options</dfn> is a struct with an struct/item named The <dfn export for=modules>webExtension</dfn> module contains functionality for managing and interacting with web extensions. {^remote end definition^}

```cddl
WebExtensionCommand = (
  webExtension.Install //
  webExtension.Uninstall
)
```

{^local end definition^}

```cddl
WebExtensionResult = (
  webExtension.InstallResult /
  webExtension.UninstallResult
)
```


### Types ###


#### The webExtension.Extension Type ####

```cddl
webExtension.Extension = text
```


### Commands ###


#### The webExtension.install Command ####

The <code>webExtension.Extension</code> type represents a web extension id within a remote end. The <dfn export for=commands>webExtension.install</dfn> command installs a web extension in the remote end.

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


#### The webExtension.uninstall Command ####

that they will be automatically uninstalled during the next shutdown. The <dfn export for=commands>webExtension.uninstall</dfn> command uninstalls a web extension for the remote end.

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


## HTML ##


## Console ##


## CSS ##


### Determine the device pixel ratio ###


### Evaluating Media Queries ###


### The viewport meta element ###


## External specifications ##
